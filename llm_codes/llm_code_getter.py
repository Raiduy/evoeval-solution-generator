import os
import json
import sys

from huggingface_hub import get_inference_endpoint, list_inference_endpoints, AsyncInferenceClient
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv('.env')

models = {
    'code-millenials': "code-millenials-34b-utk",
    'speechless-codellama': "speechless-codellama-34b-llm-exp",
    'deepseek-coder': "deepseek-coder",
    'gpt-4': "gpt-4",
    'chatgpt': "gpt-3.5-turbo",
}

hf_prompt_template = """{sys_prompt}

### Instruction: {user_prompt}

### Response:
"""


def preprocess_response(llm, response, user_prompt=None):
    if '```python' in response:
        response = response.split('```python')[1].split('```')[0]
    else:
        if llm == 'code-millenials':
            response = user_prompt + '\n' + response.split('if __name__')[0]
        elif llm == 'speechless-codellama':
            response = user_prompt + '\n' + response

    if user_prompt.split('\n')[0] not in response:
        response = user_prompt.split('\n')[0] + '\n' + response

    print("\nResponse is\n", response)
    return response


def write_to_file(experiment, llm, code_id, response, user_prompt=None):
    out_folder = f'./{experiment}/{llm}/EvoEval_difficult/EvoEval_{code_id}'
    if not os.path.isdir(out_folder):
        os.makedirs(out_folder)

    with open(f'{out_folder}/response.txt', 'w') as w:
        w.write(response)

    code = preprocess_response(llm, response, user_prompt)

    with open(f'{out_folder}/0.py', 'w') as writer:
        writer.write(code)
    print("Written problem", code_id)


def prompt_builder(experiment, model, problem_id, prompts_data):
    user_prompt = prompts_data['user_prompt'][str(problem_id)]
    system_prompt_data = prompts_data['system_prompt']

    if experiment in ['keyword', 'platform/raspberry', 'platform/pc', 'platform/server']:
        sys_prompt = system_prompt_data[experiment]

    elif experiment == 'guideline':
        sys_prompt = system_prompt_data[experiment]['base_start']
        guideline_counter = 1
        for guideline_category in system_prompt_data[experiment]['problem'][str(problem_id)]:
            for guideline in system_prompt_data[experiment]['guidelines'][guideline_category]:
                sys_prompt += str(guideline_counter) + ". " + guideline + "\n\n"
                guideline_counter += 1
        sys_prompt += system_prompt_data[experiment]['base_end']


    if model in ['gpt-4', 'chatgpt', 'deepseek-coder']:
        prompt = [
            {
                "role": "system",
                "content": sys_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    elif model == 'code-millenials':
        prompt = hf_prompt_template.format(sys_prompt=sys_prompt, 
                                            user_prompt=user_prompt)
    elif model == 'speechless-codellama':
        prompt = hf_prompt_template.format(sys_prompt=sys_prompt, 
                                            user_prompt='\n'+user_prompt)
    else:
        return "Broken"

    print("\nPrompt is\n", prompt)
    return prompt
    

def huggingface_call(experiment, prompts_data, model, problem_id):
    endpoint = get_inference_endpoint(models[model])
    messages = prompt_builder(experiment, model, problem_id, prompts_data)
    response = endpoint.client.text_generation(messages,
                                             max_new_tokens=1200,
                                             temperature=0.01)
    user_prompt = prompts_data['user_prompt'][str(problem_id)]
    write_to_file(experiment, model, problem_id, response, user_prompt)


def openAI_call(experiment, prompts_data, model, problem_id):
    if model == 'deepseek-coder':
        deepseek_key = os.getenv('deepseek_api_key')
        client = OpenAI(api_key=deepseek_key, base_url='https://api.deepseek.com')
    else:
        openai_key = os.getenv('openAI_api_key')
        client = OpenAI(api_key = openai_key)

    response = client.chat.completions.create(
        model=models[model],
        messages = prompt_builder(experiment, model, problem_id, prompts_data),
        temperature=0.0,
        stream=False
    )
    
    response = response.choices[0].message.content
    user_prompt = prompts_data['user_prompt'][str(problem_id)]
    write_to_file(experiment, model, problem_id, response, user_prompt)


if __name__ == '__main__':
    with open('./relevant_name.json', 'r') as file:
        prompts_data = json.load(file)

    experiment = sys.argv[1]
    llm = sys.argv[2]

    problems = prompts_data["user_prompt"]

    if len(sys.argv) > 3:
        problems = []
        problems_string = sys.argv[3]
        if ',' in problems_string:
            problems.extend(problems_string.split(','))
        else:
            problems.append(problems_string)

    for problem in problems:
        print("Processing problem", problem, "through", llm)
        if ("gpt" in llm) or ("deep" in llm):
            print("OpenAI call")
            openAI_call(experiment, prompts_data, llm, problem)
        else:
            print("HuggingFace call")
            huggingface_call(experiment, prompts_data, llm, problem)


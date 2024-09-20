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
    return response


def write_to_file(llm, experiment, code_id, response, user_prompt=None):
    out_folder = f'./{experiment}/{llm}/EvoEval_difficult/EvoEval_{code_id}'
    if not os.path.isdir(out_folder):
        os.makedirs(out_folder)

    with open(f'{out_folder}/response.txt', 'w') as w:
        w.write(response)

    code = preprocess_response(llm, response, user_prompt)

    with open(f'{out_folder}/0.py', 'w') as writer:
        writer.write(code)
    print("Written problem", code_id)


def huggingface_call(model, sys_prompt, problem_id, user_prompt):
    endpoint = get_inference_endpoint(models[model])
    messages=[
            {
                "role": "system",
                "content": sys_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
    ]
    if model == 'code-millenials':
        messages = hf_prompt_template.format(sys_prompt=sys_prompt, 
                                             user_prompt=user_prompt)
    elif model == 'speechless-codellama':
        messages = hf_prompt_template.format(sys_prompt=sys_prompt, 
                                             user_prompt='\n'+user_prompt)



    response = endpoint.client.text_generation(messages,
                                             max_new_tokens=1200,
                                             temperature=0.01)
    write_to_file(model, experiment, problem_id, response, user_prompt)


def openAI_call(model, sys_prompt, problem_id, user_prompt):
    openai_key = os.getenv('openAI_api_key')
    client = OpenAI(api_key = openai_key)

    response = client.chat.completions.create(
        model=models[model],
        messages=[
            {
                "role": "system",
                "content": sys_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0,
        #max_tokens=256,
    )
    
    response = response.choices[0].message.content
    write_to_file(model, experiment, problem_id, response)


if __name__ == '__main__':
    with open('./relevant_name.json', 'r') as file:
        data = json.load(file)
    experiment = sys.argv[1]
    llm = sys.argv[2]
    sys_prompt = data["system_prompt"][experiment]

    for problem in data["user_prompt"]:
        user_prompt = data["user_prompt"][problem]
        print("Processing", problem)
        if ("gpt" in llm) or ("GPT" in llm):
            print("OpenAI call")
            openAI_call(llm, sys_prompt, problem, user_prompt)
        else:
            print("HuggingFace call")
            huggingface_call(llm, sys_prompt, problem, user_prompt)




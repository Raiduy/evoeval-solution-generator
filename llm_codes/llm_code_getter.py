import os
import json

from huggingface_hub import get_inference_endpoint, list_inference_endpoints, AsyncInferenceClient
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv('.env')

inference_endpoints = {
    'code-millenials': "code-millenials-34b-utk",
    'codellama': "speechless-codellama-34b-llm-exp"
}

#endpoint = get_inference_endpoint(inference_endpoints['code-millenials'])
def preprocess_response(llm, response):
    return response

def write_to_file(llm, experiment, code_id, response):
    out_folder = f'./{experiment}/{llm}/EvoEval_difficult/EvoEval_{code_id}'
    if not os.path.isdir(out_folder):
        os.makedirs(out_folder)
    code = preprocess_response(llm, response)
    with open(f'{out_folder}/0.py', 'w') as writer:
        writer.write(code)
    print("Written problem", code_id)


def openAI_call(sys_prompt, problem_id, user_prompt):
    openai_key = os.getenv('openAI_api_key')
    client = OpenAI(api_key = openai_key)
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
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
    
    resp = response.choices[0].message.content#.split('\\begin{code}')[1].split('\\end{code}')[0]
    write_to_file("GPT", "keyword", problem_id, resp)


if __name__ == '__main__':
    #result = endpoint.client.text_generation("How do you make a for loop in python?",
    #                                         stop_sequences=["\end{code}"],
    #                                         max_new_tokens=1400)

    #with open('./test.txt', 'w') as f:
    #    f.write(resp)
    #get_response()
    #print(result)
    with open('./relevant_name.json', 'r') as file:
        data = json.load(file)
    
    sys_prompt = data["system_prompt"]["keyword"]

    for problem in data["user_prompt"]:
        user_prompt = data["user_prompt"][problem]
        print("Processing", problem)
        openAI_call(sys_prompt, problem, user_prompt)



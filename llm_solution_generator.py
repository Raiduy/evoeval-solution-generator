import ast
import os
import pandas as pd
import re
import sys


SOLUTIONS_FOLDER = './solutions/'
EVOEVAL_DIFFICULT_IDS = ['4', '61', '79', '63', '90', '53', '66', '52', '16']
MAIN_TEMPLATE = """

{target_code}

if __name__ == '__main__':
{input_line}
    i = 0

    while(True):
        {target_name}(*inputs[i%len(inputs)])
        i += 1

"""


def get_dataset():
    df = pd.DataFrame()
    if os.path.isdir('.cache'):
        if 'difficult.csv' in os.listdir('.cache/'):
            print('Reading from cache...')
            df = pd.read_csv('.cache/difficult.csv')
    else:
        print('Creating local cache...')
        os.makedirs('.cache')
        df = pd.read_json("hf://datasets/evoeval/EvoEval_difficult/test.jsonl", lines=True)
        df.to_csv('.cache/difficult.csv', index=False)
    df = df[df['task_id'].isin(['EvoEval/'+i for i in EVOEVAL_DIFFICULT_IDS])]
    return df


def process_input_line(line):
    input = line.split("for i in ")[-1]
    input = input[:-1]
    return input


def get_code_inputs(df, id):
    test_function = df[df['task_id'] == f'EvoEval/{id}']['entry_point'].values[0]
    test_code = df[df['task_id'] == f'EvoEval/{id}']['test'].values[0]
    input_line = ''
    for line in test_code.split('\n'):
        if 'inputs' in line:
            input_line = line
            break
    return test_function, input_line


def generate_code(function, code, inputs):
    return MAIN_TEMPLATE.format(target_code=code, target_name=function, 
                                input_line=inputs)


def export_python_file(output_folder, llm, id, contents):
    if not os.path.isdir(f'{output_folder}/{llm}/'):
        os.makedirs(f'{output_folder}/{llm}/')
    with open(f'{output_folder}/{llm}/{id}.py', 'w') as writer:
        writer.write(contents)


def process_llms(solutions_folder, all_llms, output_folder):
    df = get_dataset()
    for id in EVOEVAL_DIFFICULT_IDS:
        function, inputs = get_code_inputs(df, id)
        
        for llm in all_llms:
            code_path = f"{solutions_folder}{llm}/{llm}/EvoEval_difficult/EvoEval_{id}/0.py"
            with open(code_path) as reader:
                code = reader.read()
            runnable_code = generate_code(function, code, inputs)
            export_python_file(output_folder, llm, id, runnable_code)


if __name__ == '__main__':
    solutions_folder = sys.argv[1] # SOLUTIONS_FOLDER
    output_folder = sys.argv[2] # OUTPUT_FOLDER
    if len(sys.argv) < 4:
        all_llms = os.listdir(solutions_folder)
        print("All folders:", all_llms)
    else:
        all_llms = [sys.argv[3]]

    process_llms(solutions_folder, all_llms, output_folder)

    

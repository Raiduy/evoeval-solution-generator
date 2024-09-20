import os
import pandas as pd
import shlex
import subprocess
import statistics
import sys
import time


SOLUTIONS_FOLDER = './solutions/'
OUTPUT_FOLDER = './code/'
EVOEVAL_DIFFICULT_IDS = ['4', '61', '79', '63', '90', '53', '66', '52', '16']

CODE_TEMPLATE = """
{target_code}

if __name__ == '__main__':
    inputs = {input_line}
    number_of_executions = {number_of_executions}
    inputs_len = len(inputs)

    execution_counter = 0
    inputs_counter = 0

    while execution_counter != number_of_executions:
        a = {target_name}(*inputs[inputs_counter])
        inputs_counter += 1

        if inputs_counter == inputs_len:
            inputs_counter = 0
            execution_counter += 1

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
    input_line = input_line.split('inputs = ')[1]
    input_array = eval(input_line)
    return test_function, input_array


def generate_code(function, code, inputs, executions = 1):
    return CODE_TEMPLATE.format(target_code=code, target_name=function, 
                                input_line=inputs,
                                number_of_executions=executions)


def export_python_file(output_folder, llm, id, contents):
    if not os.path.isdir(f'{output_folder}/{llm}/'):
        os.makedirs(f'{output_folder}/{llm}/')
    path = f'{output_folder}/{llm}/{id}.py'
    with open(path, 'w') as writer:
        writer.write(contents)
    return path


def get_num_exec(device, problem):
    num_exec_df = pd.read_csv(f'./{device}/num_exec.csv')
    num_exec = num_exec_df[num_exec_df['id'] == int(problem)]['num_of_executions'].values[0]
    return num_exec


def process_llms(solutions_folder, all_llms, device, experiment):
    df = get_dataset()
    for id in EVOEVAL_DIFFICULT_IDS:
        function, inputs = get_code_inputs(df, id)
        
        for llm in all_llms:
            code_path = f"./llm_codes/{experiment}/{llm}/EvoEval_difficult/EvoEval_{id}/0.py"
            with open(code_path) as reader:
                code = reader.read()
            num_of_executions = get_num_exec(device, id)
            final_code = generate_code(function, code, inputs, num_of_executions)
            export_python_file(f'./{device}/{experiment}/', llm, id, final_code)


if __name__ == '__main__':
    solutions_folder = sys.argv[1] # SOLUTIONS_FOLDER
    device = sys.argv[2]
    experiment = sys.argv[3]

    all_llms = ['gpt-4', 'code-millenials', 'speechless-codellama']

    process_llms(solutions_folder, all_llms, device, experiment)
 

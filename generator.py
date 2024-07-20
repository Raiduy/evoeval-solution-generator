from operator import index
import os
import pandas as pd
import re
import sys


SOLUTIONS_FOLDER = './solutions/'
EVOEVAL_DIFFICULT_IDS = ['61', '4', '79', '63', '90', '53', '66', '52', '16']


def get_dataset():
    df = pd.DataFrame()
    if 'difficult.csv' in os.listdir('.cache/'):
        print('Reading from cache...')
        df = pd.read_csv('.cache/difficult.csv')
    else:
        df = pd.read_json("hf://datasets/evoeval/EvoEval_difficult/test.jsonl", lines=True)
        df.to_csv('.cache/difficult.csv', index=False)
    df = df[df['task_id'].isin(['EvoEval/'+i for i in EVOEVAL_DIFFICULT_IDS])]
    return df


def process_input_line(line):
    input = line.split("for i in [")[-1]
    input = input[:-2]
    print(input)
    return "hi"


def get_code_inputs(id):
    df = get_dataset()
    test_code = df[df['task_id'] == f'EvoEval/{id}']['test'].values[0]
    input_line = ''
    for line in test_code.split('\n'):
        if 'inputs' in line:
            input_line = line
            break
    inputs = process_input_line(input_line)
    return inputs


def process_llms(solutions_folder, all_llms):
    for id in EVOEVAL_DIFFICULT_IDS:
        inputs = get_code_inputs(id)
        for llm in all_llms:
            path = f"{solutions_folder}{llm}/{llm}/EvoEval_difficult/EvoEval_{id}/0.py"
            print(path)
            #code = get_solution_code(llm, id)
            break
        break

if __name__ == '__main__':
    solutions_folder = sys.argv[1] # SOLUTIONS_FOLDER
    output_folder = sys.argv[2] # OUTPUT_FOLDER
    if len(sys.argv) < 4:
        all_llms = os.listdir(solutions_folder)
        print("All folders:", all_llms)
    else:
        all_llms = [sys.argv[3]]

    process_llms(solutions_folder, all_llms)

    

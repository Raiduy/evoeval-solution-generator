import ast
import os
import pandas as pd
import re
import sys


EVOEVAL_DIFFICULT_IDS = ['4', '61', '79', '63', '90', '53', '66', '52', '16']

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


def export_python_file(output_folder, id, contents):
    if not os.path.isdir(f'{output_folder}/canonical/'):
        os.makedirs(f'{output_folder}/canonical/')
    with open(f'{output_folder}/canonical/{id}.py', 'w') as writer:
        writer.write(contents)

if __name__ == '__main__':
    df = get_dataset()
    for i, row in df.iterrows():
        print(row['task_id'])
        print(row['canonical_solution'])
        print()
        print()
        print()
        print()
        export_python_file('./code', \
                           row['task_id'].split('EvoEval/')[1], \
                           row['canonical_solution'])
 



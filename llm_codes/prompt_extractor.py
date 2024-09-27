import ast
import os
import pandas as pd
import re
import sys
import json


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


if __name__ == '__main__':
    df = get_dataset()
    with open('./relevant_name.json', 'r') as file:
        data = json.load(file)

    for i, row in df.iterrows():
        print(row['task_id'])
        print(row['prompt'])
        print()
        print()
        print()
        data['user_prompt'][row['task_id'].split('EvoEval/')[1]] = row['prompt']

    with open('./relevant_name.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    



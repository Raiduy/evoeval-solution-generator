from operator import index
import os
import pandas as pd
import re
import sys


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
    print(['Evoeval/'+i for i in EVOEVAL_DIFFICULT_IDS])
    return df

if __name__ == '__main__':
    df = get_dataset()
    print(df)
    

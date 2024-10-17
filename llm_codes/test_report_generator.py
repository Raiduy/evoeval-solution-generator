import os
import sys
import json


def parsejson(json_path):
    experiment = json_path.split('/')[1]
    if experiment == 'platform':
        experiment += '/' + json_path.split('/')[2]

    llm = json_path.split('/')[-3]

    with open(json_path, 'r') as file:
        data = json.load(file)
    
    failed = []

    for problem in data['eval']:
        if data['eval'][problem][0]['base_status'] == 'fail':
            failed.append(problem.split('/')[1])

    return experiment, llm, failed


def generate_report():
    report = {}
    
    for root, dirs, files in os.walk("./"):
        for file in files:
            if file.endswith("_pretty.json"):
                filepath = os.path.join(root, file)
                
                experiment, llm, failed = parsejson(filepath)
                tmp = {}
                tmp[llm] = failed
                report[experiment] = tmp

    json_string = json.dumps(report, indent=4)

    with open("./test_fail_report.json", "w") as outfile: 
        outfile.write(json_string)
        #json.dump(json_string, outfile, indent=4)
    

if __name__ == '__main__':
    generate_report()


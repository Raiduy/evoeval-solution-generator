#!/bin/bash

llms=(`ls ./code/`)
touch ./code/times.csv
echo code, run > ./code/times.csv

for llm in ${llms[*]}
do
    if [[ "$llm" == "times.csv" ]]
    then
        echo "times found"
        continue 1

    fi
    problems=(`ls ./code/${llm}`)
    for problem in ${problems[*]}
    do
        echo "Processing ${llm}/${problem}"
        time_output=(`{ time python3 ./code/${llm}/${problem}; } |& grep real`)
        echo ${llm}/${problem}, ${time_output[1]} >> ./code/times.csv
    done
done


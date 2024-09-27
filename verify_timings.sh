#!/bin/bash

llms=(`ls ./server/code/`)
touch ./server/code/times.csv
echo code, run > ./server/code/times.csv

for llm in ${llms[*]}
do
    if [[ "$llm" == "times.csv" ]]
    then
        echo "times found"
        continue 1

    fi
    problems=(`ls ./server/code/${llm}`)
    for problem in ${problems[*]}
    do
        echo -n "Processing ${llm}/${problem}"
        time_output=(`{ time python3 ./server/code/${llm}/${problem}; } |& grep real`)
        echo ${llm}/${problem}, ${time_output[1]} >> ./server/code/times.csv
        echo " - ${time_output[1]}"
    done
    git add . && git commit -m "${llm} 1000 runs done" && git push
done


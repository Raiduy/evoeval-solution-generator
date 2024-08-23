#!/bin/bash

llms=(`ls ./rpi/code/`)
touch ./rpi/code/times.csv
echo code, run > ./rpi/code/times.csv

for llm in ${llms[*]}
do
    if [[ "$llm" == "times.csv" ]]
    then
        echo "times found"
        continue 1

    fi
    problems=(`ls ./rpi/code/${llm}`)
    for problem in ${problems[*]}
    do
        echo "Processing ${llm}/${problem}"
        time_output=(`{ time python3 ./rpi/code/${llm}/${problem}; } |& grep real`)
        echo ${llm}/${problem}, ${time_output[1]} >> ./rpi/code/times.csv
    done
    git add . && git commit -m "${llm} sanity runs done" && git push
done


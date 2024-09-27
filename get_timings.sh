#!/bin/bash

llms=(`ls ./server/timings/`)
touch ./server/timings/times.csv
echo code, run_0, run_1, run_2, run_3, run_4, run_5, run_6, run_7, run_8, run_9, run_10, run_11, run_12, run_13, run_14, run_15, run_16, run_17, run_18, run_19, run_20, run_21, run_22, run_23, run_24, run_25, run_26, run_27, run_28, run_29 > ./server/timings/times.csv

for llm in ${llms[*]}
do
    if [[ "$llm" == "times.csv" ]]
    then
        echo "times found"
        continue 1

    fi
    problems=(`ls ./server/timings/${llm}`)
    for problem in ${problems[*]}
    do
        echo "Processing ${llm}/${problem}"
        time_output=(`{ time python3 ./server/timings/${llm}/${problem}; } |& grep real`)
        echo -n ${llm}/${problem}, ${time_output[1]} >> ./server/timings/times.csv

        for ((i = 0; i < 29; i++))
        do
            time_output=(`{ time python3 ./server/timings/${llm}/${problem}; } |& grep real`)
            echo -n , ${time_output[1]} >> ./server/timings/times.csv
            echo "Run ${i}/29 - ${time_output[1]}"
        done
        echo >> ./server/timings/times.csv
    done
    git add . && git commit -m "${llm} runs done" && git push
done



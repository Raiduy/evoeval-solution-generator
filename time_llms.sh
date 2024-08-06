#!/bin/bash

llms=(`ls ./timings/`)

for llm in ${llms[*]}
do
    problems=(`ls ./timings/${llm}`)
    for problem in ${problems[*]}
    do
        echo $problem
    done

done


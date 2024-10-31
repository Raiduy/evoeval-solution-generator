#!/bin/bash

# if [ $# -eq 0 ]; then
#   echo "Error: No arguments provided -- expected: run.sh algo_number"
#   exit 1
# else
algos=(4 61 90)
    #algo_number=$1
  for algo_number in "${algos[@]}"; do
    echo "Running algorithm number $algo_number"
    coll_down_period=5
    repetitions=10
    echo "" > logs/$algo_number.log
    for ((i=1; i<=repetitions; i++)); do
      echo "Running origin..."
      echo "************************************" >> logs/$algo_number.log
      echo ">>> origin_$algo_number <<<" >> logs/$algo_number.log
      echo "************************************" >> logs/$algo_number.log
      echo "" >> logs/$algo_number.log
      sudo /bin/python3.10 ./runner.py origin_$algo_number >> logs/$algo_number.log
      echo "" >> logs/$algo_number.log
      echo "Cooling down..."
      sleep $coll_down_period
      echo "Running michel..."
      echo "************************************" >> logs/$algo_number.log
      echo ">>> michel_$algo_number <<<" >> logs/$algo_number.log
      echo "************************************" >> logs/$algo_number.log
      echo "" >> logs/$algo_number.log
      sudo /bin/python3.10 ./runner.py michel_$algo_number >> logs/$algo_number.log
      echo "Cooling down..."
      sleep $coll_down_period
    done
  done
# fi
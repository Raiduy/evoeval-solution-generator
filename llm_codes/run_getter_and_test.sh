## $1 experiment
## $2 llm
## $3 problem or list of problems (optional)

tab=$( echo -e "\t" )

if [ -z "$3" ]; then
    python3 llm_code_getter.py $1 $2  
    python3 ../../evoeval/evoeval/evaluate.py --dataset EvoEval_difficult --samples ./$1/$2/EvoEval_difficult/ 
    python3 -m json.tool ./$1/$2/EvoEval_difficult/eval_results.json &> ./$1/$2/EvoEval_difficult/eval_results_pretty.json
    
else
    for ((i = 1; i < 7; i++)); do
        echo "Iteration $i out of 6."
    
        echo "Reprompting problem(s) $3, from experiment $1, $2..."
        mkdir -p ./$1/$2/retries/
        python3 llm_code_getter.py $1 $2 $3 >> ./$1/$2/retries/$3.log
        rm -f ./$1/$2/EvoEval_difficult/eval_results.json
        python3 ../../evoeval/evoeval/evaluate.py --dataset EvoEval_difficult --samples ./$1/$2/EvoEval_difficult/ | grep 'pass' >> ./$1/$2/retries/$3.log
        echo $( tail -n 1 ./$1/$2/retries/$3.log )
        if [[ "pass@1:${tab}1.000" == "$( tail -n 1 ./$1/$2/retries/$3.log )" ]]; then
            echo "Retries successful, breaking loop"
            python3 -m json.tool ./$1/$2/EvoEval_difficult/eval_results.json &> ./$1/$2/EvoEval_difficult/eval_results_pretty.json
            break
        fi
        python3 -m json.tool ./$1/$2/EvoEval_difficult/eval_results.json &>> ./$1/$2/retries/$3.json
        python3 -m json.tool ./$1/$2/EvoEval_difficult/eval_results.json &> ./$1/$2/EvoEval_difficult/eval_results_pretty.json
        echo "" >> ./$1/$2/retries/$3.log
        echo "---------------------------------------------------" >> ./$1/$2/retries/$3.log
        echo "" >> ./$1/$2/retries/$3.log
    done
fi

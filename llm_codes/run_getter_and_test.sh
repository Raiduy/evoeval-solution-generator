## $1 experiment
## $2 llm

python3 llm_code_getter.py $1 $2
python3 ../../evoeval/evoeval/evaluate.py --dataset EvoEval_difficult --samples ./$1/$2/EvoEval_difficult/
python3 -m json.tool ./$1/$2/EvoEval_difficult/eval_results.json &> ./$1/$2/EvoEval_difficult/eval_results_pretty.json


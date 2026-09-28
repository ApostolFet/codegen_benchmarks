rm -f files/conditon/base.json files/conditon/codegen.json files/conditon/separate_func.json
echo "=== Condition base benchmark ==="
python -m banchmarks.condition.base -o files/conditon/base.json --quiet
echo "================================"
echo "=== Condition codegen benchmark ==="
python -m banchmarks.condition.codegen -o files/conditon/codegen.json --quiet
echo "================================"
echo "=== Condition separate func benchmark ==="
python -m banchmarks.condition.separate_func -o files/conditon/separate_func.json --quiet
echo "================================"
pyperf compare_to files/conditon/base.json files/conditon/codegen.json files/conditon/separate_func.json --table

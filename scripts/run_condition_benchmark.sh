rm -f files/condition/base.json files/condition/codegen.json files/condition/separate_func.json
echo "=== Condition base benchmark ==="
python -m codegen_benchmarks.condition.base -o files/condition/base.json --quiet
echo "================================"
echo "=== Condition codegen benchmark ==="
python -m codegen_benchmarks.condition.codegen -o files/condition/codegen.json --quiet
echo "================================"
echo "=== Condition separate func benchmark ==="
python -m codegen_benchmarks.condition.separate_func -o files/condition/separate_func.json --quiet
echo "================================"
pyperf compare_to files/condition/base.json files/condition/codegen.json files/condition/separate_func.json --table

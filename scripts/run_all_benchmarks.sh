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

rm -f files/loop/base.json files/loop/codegen.json
echo "=== Loop base benchmark ==="
python -m codegen_benchmarks.loop.base -o files/loop/base.json --quiet
echo "================================"
echo "=== Loop codegen benchmark ==="
python -m codegen_benchmarks.loop.codegen -o files/loop/codegen.json --quiet
echo "================================"

rm -f files/dishka_wrap_injection/base.json files/dishka_wrap_injection/codegen.json
echo "=== dishka wrap_injection base benchmark ==="
pip install -r src/codegen_benchmarks/dishka_wrap_injection/base_version.txt
python -m codegen_benchmarks.dishka_wrap_injection.base -o files/dishka_wrap_injection/base.json --quiet
echo "================================"
echo "=== dishka wrap_injection codegen benchmark ==="
pip install -r src/codegen_benchmarks/dishka_wrap_injection/codegen_version.txt
python -m codegen_benchmarks.dishka_wrap_injection.base -o files/dishka_wrap_injection/codegen.json --quiet
echo "================================"

pyperf compare_to files/condition/base.json files/condition/codegen.json files/condition/separate_func.json --table
pyperf compare_to files/loop/base.json files/loop/codegen.json --table
pyperf compare_to files/dishka_wrap_injection/base.json files/dishka_wrap_injection/codegen.json --table

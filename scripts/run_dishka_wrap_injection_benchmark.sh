rm -f files/dishka_wrap_injection/base.json files/dishka_wrap_injection/codegen.json
echo "=== dishka wrap_injection base benchmark ==="
pip install -r src/codegen_benchmarks/dishka_wrap_injection/base_version.txt
python -m codegen_benchmarks.dishka_wrap_injection.base -o files/dishka_wrap_injection/base.json --quiet
echo "================================"
echo "=== dishka wrap_injection codegen benchmark ==="
pip install -r src/codegen_benchmarks/dishka_wrap_injection/codegen_version.txt
python -m codegen_benchmarks.dishka_wrap_injection.base -o files/dishka_wrap_injection/codegen.json --quiet
echo "================================"
pyperf compare_to files/dishka_wrap_injection/base.json files/dishka_wrap_injection/codegen.json --table

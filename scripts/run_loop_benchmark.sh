rm -f files/loop/base.json files/loop/codegen.json
echo "=== Loop base benchmark ==="
python -m banchmarks.loop.base -o files/loop/base.json --quiet
echo "================================"
echo "=== Loop codegen benchmark ==="
python -m banchmarks.loop.codegen -o files/loop/codegen.json --quiet
echo "================================"
pyperf compare_to files/loop/base.json files/loop/codegen.json --table

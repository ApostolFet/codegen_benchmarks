from collections.abc import Callable
from typing import Any

from codegen_benchmarks.base import run_benchmark


def start_up() -> dict[str, Any]:
    def generate_get_result(integers: list[int]) -> Callable[[float], float]:
        indent = "   "
        next_row = "\n"
        code = ["def get_result(user_input):", next_row, indent, "result = user_input"]
        for i in integers:
            code += [next_row, indent, "result += ", str(i)]

        code += [next_row, indent, "return result"]
        globals = {}
        exec("".join(code), globals)
        return globals["get_result"]

    integers = [i for i in range(1000)]

    get_result = generate_get_result(integers)

    def main() -> None:
        get_result(1000)

    return {"get_result": get_result, "main": main}


if __name__ == "__main__":
    run_benchmark(name="loop", start_up=start_up)

from collections.abc import Callable
from typing import Any

from codegen_benchmarks.base import run_benchmark


def start_up() -> dict[str, Any]:
    def generate_get_result(
        is_divide: bool, is_round: bool
    ) -> Callable[[float], float]:
        indent = "   "
        next_row = "\n"
        code = ["def get_result(user_input):"]
        if is_divide:
            code += [next_row, indent, "user_input = user_input / 2"]

        if is_round:
            code += [next_row, indent, "user_input = round(user_input)"]

        code += [next_row, indent, "return user_input * 11"]
        globals = {}
        exec("".join(code), globals)
        return globals["get_result"]

    is_divide = True
    is_round = True

    get_result = generate_get_result(is_divide, is_round)

    def main() -> None:
        get_result(1000)

    return {"get_result": get_result, "main": main}


if __name__ == "__main__":
    run_benchmark(name="condition", start_up=start_up)

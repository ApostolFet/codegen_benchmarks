
from typing import Any

from codegen_benchmarks.base import run_benchmark


def start_up() -> dict[str, Any]:
    def get_result(user_input: float, is_devide: bool, is_round: bool) -> float:

        if is_devide:
            user_input = user_input / 2

        if is_round:
            user_input = round(user_input)

        return user_input * 11


    is_devide = True
    is_round = True

    def main() -> None:
        get_result(1000, is_devide=is_devide, is_round=is_round)

    return {"get_result": get_result, "main": main}


if __name__ == "__main__":
    run_benchmark(name="condition", start_up=start_up)

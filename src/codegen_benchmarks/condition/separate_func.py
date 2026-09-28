from typing import Any

from codegen_benchmarks.base import run_benchmark


def start_up() -> dict[str, Any]:
    def func_with_devide(user_input: float) -> float:
        user_input = user_input / 2
        return user_input * 11

    def func_with_round(user_input: float) -> float:
        user_input = round(user_input)
        return user_input * 11

    def func_with_round_and_devide(user_input: float) -> float:
        user_input = user_input / 2
        user_input = round(user_input)
        return user_input * 11

    def func_with_out_round_and_devide(user_input: float) -> float:
        return user_input * 11

    dispatch_dict = {
        (False, False): func_with_out_round_and_devide,
        (True, False): func_with_round,
        (False, True): func_with_devide,
        (True, True): func_with_round_and_devide,
    }

    is_devide = True
    is_round = True

    get_result = dispatch_dict[(is_devide, is_round)]

    def main() -> None:
        get_result(1000)

    return {"get_result": get_result, "main": main}


if __name__ == "__main__":
    run_benchmark(name="condition", start_up=start_up)

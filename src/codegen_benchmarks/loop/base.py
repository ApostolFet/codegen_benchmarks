from typing import Any

from codegen_benchmarks.base import run_benchmark


def start_up() -> dict[str, Any]:
    def get_result(user_input: float, integers: list[int]) -> float:
        result = user_input
        for i in integers:
            result += i

        return result

    integers = [i for i in range(1000)]

    def main() -> None:
        get_result(1000, integers=integers)

    return {"get_result": get_result, "main": main}


if __name__ == "__main__":
    run_benchmark(name="loop", start_up=start_up)

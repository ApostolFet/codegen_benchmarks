from collections.abc import Callable
from typing import Any

import pyperf


def run_benchmark(*, name: str, start_up: Callable[[], dict[str, Any]]) -> None:
    runner = pyperf.Runner(min_time=0.5)

    runner.timeit(
        name=f"{name}/runtime",
        stmt="main()",
        globals=start_up(),
    )

    runner.timeit(
        name=f"{name}/startup",
        stmt="start_up()",
        globals={"start_up": start_up},
    )

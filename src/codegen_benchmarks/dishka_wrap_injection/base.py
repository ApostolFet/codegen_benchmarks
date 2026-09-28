from typing import Any

from codegen_benchmarks.base import run_benchmark


def start_up() -> dict[str, Any]:
    from inspect import Parameter
    from dishka.integrations.base import wrap_injection
    from dishka import Container, FromDishka, Provider, Scope, make_container, provide

    class MyProvider(Provider):
        scope = Scope.REQUEST

        get_str = provide(lambda self: "1", provides=str)
        get_int = provide(lambda self: 1, provides=int)

    container = make_container(MyProvider())

    def inject(func):
        return wrap_injection(
            func=func,
            container_getter=lambda args, kwargs: container,
            manage_scope=True,
            additional_params=[
                Parameter(
                    "dishka_container",
                    kind=Parameter.KEYWORD_ONLY,
                    annotation=Container,
                )
            ],
        )

    @inject
    def my_func(x: FromDishka[str], y: FromDishka[int]):
        pass

    def main():
        my_func(dishka_container=container)

    return {"main": main}


if __name__ == "__main__":
    run_benchmark(name="dishka_wrap_injection", start_up=start_up)

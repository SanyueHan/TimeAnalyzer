from analyzer.diagnose import explain_performance_by_class, explain_performance_by_name
from test.python_built_in.examples.filter import Filter
from test.python_built_in.examples.sum import Sum


LIMIT = 1000000


if __name__ == "__main__":
    for cls in (
        Sum,
        Filter
    ):
        cls(LIMIT).run()

    print(f"Limit = {LIMIT}")
    explain_performance_by_name()
    explain_performance_by_class()

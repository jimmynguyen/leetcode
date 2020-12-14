def run_tests(solutions,tests,equals=None):
    for solution in solutions:
        for i,(inputs,expected) in enumerate(tests):
            actual = solution(*inputs)
            comparison = actual == expected if equals is None else equals(actual,expected)
            assert comparison,f"failed test case {i+1}: solution={solution} inputs={inputs}, expected={expected}, actual={actual}"
        print(f"passed all tests for {solution.__name__}")
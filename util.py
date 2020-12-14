def run_tests(solutions,tests,equals=None):
    for i,(inputs,expected) in enumerate(tests):
        for solution in solutions:
            actual = solution(*inputs)
            comparison = actual == expected if equals is None else equals(actual,expected)
            assert comparison,f"failed test case {i+1}: solution={solution} inputs={inputs}, expected={expected}, actual={actual}"
    print("passed all tests")
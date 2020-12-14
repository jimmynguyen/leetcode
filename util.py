def run_tests(solutions,tests):
    for i,(test,expected) in enumerate(tests):
        for solution in solutions:
            actual = solution(*test)
            assert actual == expected,f"failed test case {i+1}: solution={solution} inputs={test}, expected={expected}, actual={actual}"
    print("passed all tests")
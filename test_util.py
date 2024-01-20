def run_a_test_many_times(test, iterations=10, show_stat=True, test_args={}):
    succeed = 0
    for i in range(iterations):
        if not test(**test_args):
           continue
        succeed += 1

    if show_stat:
        print(f"Succeed {round(succeed/iterations * 100, 2)} %")
    return succeed == iterations
    
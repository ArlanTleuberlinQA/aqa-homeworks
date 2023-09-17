import time


def decorator_1(f):
    def do_sum_1(a, b):
        start = time.time()
        result = f(a, b)
        end = time.time()
        exe = end - start
        print(f"Виконано за {exe} з результатом: {result}")
        return result

    return do_sum_1


@decorator_1
def some_function(a, b):
    time.sleep(1)
    return a + b


some_function(10, 20)

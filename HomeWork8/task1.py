def decorator(f):
    def do_sum(a, b):
        result = f(a, b)
        print(f"Викликано функцію {f.__name__} з результатом: {result}")
        return result

    return do_sum


@decorator
def plus(a, b):
    return a + b

plus(10,40)


@decorator
def sqr(a, b):
    return a * b


sqr(30, 10)

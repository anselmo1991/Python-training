import time
import functools


def timeit(threshold=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            if threshold is None or execution_time > threshold:
                print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
            return result
        return wrapper
    return decorator


# Пример использования декоратора
@timeit(threshold=0.5)
def some_heavy_function():
    time.sleep(0.6)
    print("Some heavy function executed.")


@timeit()
def another_function():
    time.sleep(0.2)
    print("Another function executed.")


if __name__ == "__main__":
    some_heavy_function()
    another_function()

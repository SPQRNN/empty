def fib(n):
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci({i}) = {fib(i)}")
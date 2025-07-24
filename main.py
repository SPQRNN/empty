from fibonacci import fib

def main():
    """Print the first 10 Fibonacci numbers."""
    for i in range(1, 11):
        print(f"Fib({i}) = {fib(i)}")

if __name__ == "__main__":
    main()
def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to calculate.

    Returns:
    int: The nth Fibonacci number.

    Raises:
    TypeError: If n is not an integer.
    ValueError: If n is a negative integer.
    """

    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize the Fibonacci sequence
    a, b = 0, 1

    # Calculate the nth Fibonacci number
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.utils.math import fibonacci

# Define the Fibonacci request model
class FibonacciRequest(BaseModel):
    n: int

app = FastAPI()

@app.post("/fibonacci", response_model=int)
async def calculate_fibonacci(request: FibonacciRequest):
    """
    Calculate the nth Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to calculate.

    Returns:
    int: The nth Fibonacci number.

    Raises:
    HTTPException: If n is a negative integer or not an integer.
    """

    if not isinstance(request.n, int):
        raise HTTPException(status_code=400, detail="n must be an integer")
    if request.n < 0:
        raise HTTPException(status_code=400, detail="n must be a non-negative integer")

    return fibonacci(request.n)
import numpy as np
from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get("/multiply_matrices")
def multiply_matrices():
    # Generate random matrices
    matrix_a = np.random.rand(10, 10)
    matrix_b = np.random.rand(10, 10)

    # Multiply matrices
    product = np.dot(matrix_a, matrix_b)

    # Return dictionary
    return {
        "matrix_a": matrix_a.tolist(),
        "matrix_b": matrix_b.tolist(),
        "product": product.tolist()
    }
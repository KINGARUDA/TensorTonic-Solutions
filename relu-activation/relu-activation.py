import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    xs = np.asarray(x)
    y = np.maximum(0.0, x)

    return np.asarray(y)
    pass
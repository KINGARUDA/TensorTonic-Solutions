import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    xs = np.array(x)
    y = 1 / (1 + np.exp(-xs))

    return y
    pass
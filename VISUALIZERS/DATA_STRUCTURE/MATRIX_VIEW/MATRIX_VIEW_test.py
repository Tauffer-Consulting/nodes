import numpy as np

from functools import wraps
from unittest.mock import patch


def mock_flojoy_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function


patch("flojoy.flojoy", mock_flojoy_decorator).start()

import MATRIX_VIEW
from PYTHON.nodes.GENERATORS.SIMULATIONS.MATRIX.MATRIX import MATRIX


def test_MATRIX_VIEW():
    try:
        # generate a MATRIX that has different number of rows and columns
        m1 = MATRIX([], {"row": 3, "column": 4})

        # run MATRIX_VIEW function
        MATRIX_VIEW.MATRIX_VIEW([m1], {})
    except:
        raise AssertionError("Unable visualize the matrix")

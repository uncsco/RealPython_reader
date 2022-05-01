import pytest

import mypkg

def test__version():
    assert len(mypkg.__version__) > 0

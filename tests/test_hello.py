import pytest
from example.hello import inc


def test_inc():
    assert inc(5) == 6
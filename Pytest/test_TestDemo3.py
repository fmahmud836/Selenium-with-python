import pytest
from _pytest.fixtures import fixture


@fixture()
def setUp():
    print("Once before everything")
    yield
    print("Once before everything")


def testMethod1(setUp):
    print("1 ")

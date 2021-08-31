import pytest


@pytest.fixture()
def setUp():
    print("Once before everything")


@pytest.yield_fixture()
def close():
    print("Close")


def testMethod1(setUp):
    print("1 ")


def testMethod2(close):
    print("2")

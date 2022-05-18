import pytest
from pyby import EnumerableDict, EnumerableList
from .test_helpers import Seen


@pytest.fixture
def enumerable_dict():
    return EnumerableDict(a=1, b=2, c=3)


@pytest.fixture
def empty_dict():
    return EnumerableDict()


@pytest.fixture
def empty_list():
    return EnumerableList()


@pytest.fixture
def numbers():
    return EnumerableList([1, 2, 3])


@pytest.fixture
def seen():
    return Seen()

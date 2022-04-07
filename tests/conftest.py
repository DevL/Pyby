import pytest
from .test_helpers import Seen


@pytest.fixture
def seen():
    return Seen()

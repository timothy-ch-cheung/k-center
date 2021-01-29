import random

import pytest


@pytest.fixture
def seed_random():
    random.seed(0)

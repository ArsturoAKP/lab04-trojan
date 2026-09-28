import pytest
from bank import BankAccount

@pytest.fixture
def funded_account():
    return BankAccount(1000)
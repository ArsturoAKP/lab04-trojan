import pytest
from bank import BankAccount
@pytest.fixture
def account():
    return BankAccount(100)
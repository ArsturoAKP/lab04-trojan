import pytest
from bank import BankAccount
@pytest.fixture
def account():
    print("[setup]")
    account = BankAccount(100)
    yield account
    print("[teardown]")
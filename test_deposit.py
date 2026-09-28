import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)

def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150

def test_deposit_returns_new_balance(account):
    result = account.deposit(25)
    assert result == 125

def test_deposit_multiple_times(account):
    account.deposit(50)
    account.deposit(25)
    assert account.balance == 175

def test_deposit_negative_amount_raises_error(account):
    with pytest.raises(ValueError, match="Deposit must be positive"):
        account.deposit(-20)

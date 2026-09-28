def test_shared_account_has_initial_balance(funded_account):
    assert funded_account.balance == 1000

def test_shared_account_can_withdraw(funded_account):
    funded_account.withdraw(200)
    assert funded_account.balance == 800
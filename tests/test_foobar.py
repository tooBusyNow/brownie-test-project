from operator import contains
import pytest
from brownie import FooBaseToken, accounts

@pytest.fixture
def contract():
    return FooBaseToken.deploy(1333777, {'from' : accounts[0]})


def test_transfer(contract):
    contract.transfer(accounts[1], 777, {'from' : accounts[0]})
    assert contract.balanceOf(accounts[1]) == 777

def test_destruct(contract):
    pass

def test_fallback(contract):
    pass

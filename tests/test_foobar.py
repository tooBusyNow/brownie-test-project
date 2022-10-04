from operator import contains
import pytest
from brownie import FooBaseToken, accounts

@pytest.fixture
def contract():
    return FooBaseToken.deploy(1333777, {'from' : accounts[0]})


def test_transfer(contract):
    contract.transfer(accounts[1], 777, {'from' : accounts[0]})
    assert contract.balanceOf(accounts[1]) == 777

def test_mint(contract):
    contract.mint(150, accounts[1], {'from' : accounts[0]})
    assert contract.totalSupply() == 1333777 + 150
    assert contract.balanceOf(accounts[1]) == 150

def test_burn(contract):
    contract.burn(1000500, accounts[0], {"from" : accounts[0]})
    assert contract.totalSupply() == 1333777 - 1000500
    assert contract.balanceOf(accounts[0]) == 1333777 - 1000500


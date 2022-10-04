from brownie import FooBaseToken, accounts

def main(): 
    goerli_acc = accounts.load('goerli-main')
    FooBaseToken.deploy(123456789, {'from' : goerli_acc})
    
    print('Have successfully deployed')
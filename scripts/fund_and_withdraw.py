from brownie import FundMe
from scripts.helpfull_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entranceFee = fund_me.getEntranceFee()
    fund_me.fund({
        "from" : account, "value": entranceFee
    })

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from":account})

def main():
    fund()
    withdraw()
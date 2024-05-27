
from brownie import accounts, FundMe, network
from scripts.helpfull_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fundme
import pytest


def test_can_fund_and_withdraw():
    fund_me = deploy_fundme()
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    txn = fund_me.fund({
        "from":account, "value":entrance_fee
    })
    txn.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    txn2 = fund_me.withdraw({"from":account})
    assert fund_me.addressToAmountFunded(account.address) == 0

def test_only_owner_can_withdraw():
    if(network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        pytest.skip("only for local environments")
    account = get_account()
    fund_me = deploy_fundme()
    bad_actor = accounts.add()
    fund_me.withdraw({"from":bad_actor})



from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 2000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
MAINNET_FORK = ["mainnet-fork-eth"]

def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in MAINNET_FORK):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mocks():
    if(len(MockV3Aggregator) <= 0):
            MockV3Aggregator.deploy(DECIMALS, Web3.to_wei(STARTING_PRICE, "ether"), {"from" : get_account()})
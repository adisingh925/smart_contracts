from brownie import FundMe, config, network, MockV3Aggregator
from scripts.helpfull_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fundme():
    account = get_account()

    if(network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        price_feed = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed = MockV3Aggregator[-1].address

    fundme = FundMe.deploy(price_feed,{"from" : account}, publish_source=config["networks"][network.show_active()].get("verify"))

    return fundme

def main():
    deploy_fundme()
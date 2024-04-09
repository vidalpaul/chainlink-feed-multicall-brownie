# call the last 50 rounds in a Chainlink price feed in a single call
from brownie import Contract, interface, multicall
from os import getenv

def main():
    # Create a Chainlink price feed contract object
    price_feed = Contract.from_abi(
        "PriceFeed", 
        address=getenv('PRICE_FEED_ADDRESS'), 
        abi=interface.AggregatorV3Interface.abi
        )
    
    rounds = []
    latest_round = price_feed.latestRoundData()[0]

    multicall(
        address=getenv('MULTICALL_ADDRESS'),
    )

    with multicall:
        for i in range(latest_round, latest_round - 50, -1):
            rounds.append(price_feed.getRoundData(i))

    
    print(rounds)
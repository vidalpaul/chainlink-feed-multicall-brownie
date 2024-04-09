# call the last 50 rounds in a Chainlink price feed in a single call
# and plot the results using matplotlib
from brownie import Contract, interface, multicall
from datetime import datetime
import matplotlib.pyplot as plt
from os import getenv

def main():
    # Create a Chainlink price feed contract object
    price_feed = Contract.from_abi(
        "PriceFeed", 
        address=getenv('PRICE_FEED_ADDRESS'), 
        abi=interface.AggregatorV3Interface.abi
        )

    latest_round = price_feed.latestRoundData()[0]
    decimals = price_feed.decimals()

    answers, timestamps = [], []

    with multicall(address=getenv('MULTICALL_ADDRESS')):
        for i in range(latest_round, latest_round - 50, -1):
            answers.append(price_feed.getRoundData(i)[1] / 10 ** decimals)
            timestamps.append(datetime.fromtimestamp(price_feed.getRoundData(i)[3]))
    
    plt.plot(timestamps, answers)
    plt.show()
    

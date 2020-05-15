import time
import threading
from reader import DataReader

class MarketSimulator:
    def __init__(self, data_dir, start_day, limit_fee, market_fee, liquidation_fee):
        self.start_time = time.time()
        self.timesteps = 0
        self.miner = DataReader(data_dir, start_day)
        self.fee = (limit_fee, market_fee, liquidation_fee)
        self.queuedOrders = []
        self.orderbook = {'buy':[], 'sell':[]}

# model form
# model is class that has action selector, trainer(only ml model), report generator
# next() class method gets current env and generate propriate action return form is action
# get_report() class method returns model report

    def __check_order_sequence(self, side, price, sequence):
        pass

    #order form : order = {'num': 2, 'side': 'buy', 'price': 8394.3, 'quantity': 50, 'sequence': 3245}
    def check_order(self, order):
        if order['side'] == 'buy':
            if order['price'] > self.bestbuy:
                return 1
            elif order['price'] == self.bestbuy:
                return self.__check_order_sequence(order['side'], order['price'], order['sequence'])
            else:
                return 0
        else:
            if order['price'] < self.bestsell:
                return 1
            elif order['price'] == self.bestsell:
                return self.__check_order_sequence(order['side'], order['price'], order['sequence'])
            else:
                return 0

# data form
# data = {'orderbook': [], 'trades': [], '}
    def next(self):
        data = self.miner.next_data()
        self.timesteps += 1
        for order in self.queuedOrders:


    def print_report(self):
        current_time = time.time()
        print("Elapsed time: ", current_time - self.start_time)
        print("Timesteps: ", self.timesteps)

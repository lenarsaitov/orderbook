from collections import defaultdict
import json
from pprint import pprint

class OrderBook:
    def __init__(self):
        self.ask_prices = []
        self.ask_quantity = defaultdict(list)
        self.bid_prices = []
        self.bid_quantity = defaultdict(list)

        self.bids = defaultdict(list)
        self.asks = defaultdict(list)

        self.initial_order = []
        self.spred = None
        self.order_id = 0

    def raise_order_id(self):
        self.order_id += 1
        return self.order_id

    @property
    def max_bid(self):
        return max(self.bids) if self.bids else 0

    @property
    def min_ask(self):
        return min(self.asks) if self.asks else float('inf')

    def put_order(self, order):
        self.initial_order.append(order)
        order.order_id = self.raise_order_id()

        if order.side == 0:
            self.bids[order.price].append(order)
        else:
            self.asks[order.price].append(order)

    def get_order(self, index):
        for price in self.bids.keys():
            for j in self.bids[price]:
                if index == j.order_id:
                    # print(f"id: {j.order_id}, quantity: {j.quantity}, price: {j.price} ")
                    return (j.order_id, j.quantity, j.price)

        for price in self.asks.keys():
            for j in self.asks[price]:
                if index == j.order_id:
                    # print(f"id: {j.order_id}, quantity: {j.quantity}, price: {j.price} ")
                    return (j.order_id, j.quantity, j.price)

    def delete_order(self, index):
        for i in self.bids.keys():
            for j in self.bids[i]:
                if index == j.order_id:
                    self.bids[i].remove(j)

        for i in self.asks.keys():
            for j in self.asks[i]:
                if index == j.order_id:
                    self.asks[i].remove(j)

    def present_orderbook_with_each_order(self):
        self.bid_prices = sorted(self.bids.keys(), reverse=True)
        self.ask_prices = sorted(self.asks.keys())

        print()
        print("|  Id   |  Quantity  |    Price    |")
        print('====================================')
        if len(self.ask_prices) == 0:
            print('                Empty             ')

        for i in reversed(self.ask_prices):
            for j in self.asks[i]:
                print(f"|   {j.order_id}   |      {j.quantity}     |     {j.price}     |")
        print('====================================')
        if len(self.bid_prices) == 0:
            print('                Empty             ')

        for i in self.bid_prices:
            for j in self.bids[i]:
                print(f"|   {j.order_id}   |      {j.quantity}     |     {j.price}     |")

    def aggregation_orders(self):
        self.bid_prices = sorted(self.bids.keys(), reverse=True)
        self.ask_prices = sorted(self.asks.keys())
        self.bid_quantities = [sum(o.quantity for o in self.bids[p]) for p in self.bid_prices]
        self.ask_quantities = [sum(o.quantity for o in self.asks[p]) for p in self.ask_prices]

    def snapshot_market(self):
        self.aggregation_orders()
        data = defaultdict(list)
        asks_table = []
        bids_table = []

        for i, price in reversed(list(enumerate(self.ask_prices))):
            dict_order = {}
            dict_order['price'] = self.ask_prices[i]
            dict_order['quantity'] = self.ask_quantities[i]
            data['asks'].append(dict_order)
            asks_table.append([self.ask_prices[i], self.ask_quantities[i]])

        for i, price in enumerate(self.bid_prices):
            dict_order = {}
            dict_order['price'] = self.bid_prices[i]
            dict_order['quantity'] = self.bid_quantities[i]
            data['bids'].append(dict_order)
            bids_table.append([self.bid_prices[i], self.bid_quantities[i]])

        data_json = json.dumps(data)

        with open("data_file.json", "w") as write_file:
            json.dump(data_json, write_file)

        return asks_table, bids_table

    def read_json(self):
        with open("data_file.json", "r") as f:
            text = json.load(f)
            pprint(text)

class Order:
    def __init__(self, side, price, quantity):
        # first argument: 1 for sell, 0 for buy
        self.side = side
        self.price = price
        self.quantity = quantity
        self.order_id = None

if __name__ == '__main__':
    print("..start main process..")
    # ob = OrderBook()
    #
    # orders = [Order(0, 61.57, 20),
    #           Order(0, 57.23, 20),
    #           Order(1, 62.55, 10),
    #           Order(0, 60.23, 5),
    #           Order(0, 61.40, 25),
    #           Order(1, 61.91, 10),
    #           Order(0, 59.95, 25),
    #           Order(1, 62.11, 15),
    #           Order(1, 62.11, 15),
    #           Order(1, 62.11, 15)
    #           ]
    #
    # for order in orders:
    #     ob.put_order(order)
    #
    # print(ob.get_order(2))
    # ob.snapshot_market()
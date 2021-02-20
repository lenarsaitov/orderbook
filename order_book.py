from collections import defaultdict

class OrderBook:
    def __init__(self):
        self.ask_prices = []
        self.ask_quantity = defaultdict(list)
        self.bid_prices = []
        self.bid_quantity = defaultdict(list)

        self.bids = defaultdict(list)
        self.asks = defaultdict(list)

        self.initial_order = []
        self.spred = 0
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

    def delete_order(self, index):
        for i in self.bids.keys():
            for j in self.bids[i]:
                if index == j.order_id:
                    self.bids[i].remove(j)

        for i in self.asks.keys():
            for j in self.asks[i]:
                if index == j.order_id:
                    self.asks[i].remove(j)

    def present_orderbook(self):
        self.bid_prices = sorted(self.bids.keys(), reverse=True)
        self.ask_prices = sorted(self.asks.keys())

        for price in self.bid_prices:
            sum_order_this_price = 0
            for orders in self.bids[price]:
                sum_order_this_price += orders.quantity
            self.bid_quantity[price].append(sum_order_this_price)

        for price in self.ask_prices:
            sum_order_this_price = 0
            for orders in self.asks[price]:
                sum_order_this_price += orders.quantity
            self.ask_quantity[price].append(sum_order_this_price)

        # self.bid_quantities = [sum(k.size for k in self.bids[t]) for t in self.bid_prices]
        # self.ask_quantities = [sum(k.size for k in self.asks[t]) for t in self.ask_prices]

        print("|  Id   |  Quantity  |    Price    |")
        print('====================================')
        if len(self.ask_prices) == 0:
            print('                Empty             ')

        for i in reversed(self.ask_prices):
            for j in self.asks[i]:
                print(f"|   {j.order_id}   |      {self.ask_quantity[j.price][0]}     |     {j.price}     |")
        print('====================================')
        if len(self.bid_prices) == 0:
            print('                Empty             ')

        for i in self.bid_prices:
            for j in self.bids[i]:
                print(f"|   {j.order_id}   |      {j.quantity}     |     {j.price}     |")

class Order:
    def __init__(self, side, price, quantity):
        # first argument: 1 for sell, 0 for buy
        self.side = side
        self.price = price
        self.quantity = quantity
        self.order_id = None

if __name__ == '__main__':
    ob = OrderBook()

    orders = [Order(0, 61.57, 20),
              Order(0, 57.23, 20),
              Order(1, 62.55, 10),
              Order(0, 60.23, 5),
              Order(0, 61.40, 25),
              Order(1, 61.91, 10),
              Order(0, 59.95, 25),
              Order(1, 62.11, 15),
              Order(1, 62.11, 15),
              Order(1, 62.11, 15)
              ]

    for order in orders:
        ob.put_order(order)

    print(ob.asks)
    print(ob.bids)

    # for i in ob.bids.keys():
    #     for j in ob.bids[i]:
    #         print(j.order_id)
    # print("__")
    # for i in ob.asks.keys():
    #     for j in ob.asks[i]:
    #         print(j.order_id)

    print("____")

    # ob.delete_order(8)
    # ob.delete_order(1)
    # ob.delete_order(4)

    # for i in ob.bids.keys():
    #     for j in ob.bids[i]:
    #         print(j.order_id)
    # print("__")
    # for i in ob.asks.keys():
    #     for j in ob.asks[i]:
    #         print(j.order_id)

    ob.present_orderbook()
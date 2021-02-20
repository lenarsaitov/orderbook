from collections import defaultdict

class OrderBook:
    def __init__(self):
        self.ask_prices = []
        self.ask_quantity = []
        self.bid_prices = []
        self.bid_quantity = []

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
        ob.initial_order.append(order)
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
        pass

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
              Order(1, 62.11, 15)]

    for order in orders:
        ob.put_order(order)

    print(ob.asks)
    print(ob.bids)

    for i in ob.bids.keys():
        for j in ob.bids[i]:
            print(j.order_id)
    print("__")
    for i in ob.asks.keys():
        for j in ob.asks[i]:
            print(j.order_id)

    print("____")

    ob.delete_order(8)
    ob.delete_order(1)
    ob.delete_order(4)

    for i in ob.bids.keys():
        for j in ob.bids[i]:
            print(j.order_id)
    print("__")
    for i in ob.asks.keys():
        for j in ob.asks[i]:
            print(j.order_id)
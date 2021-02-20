

class OrderBook:
    def __init__(self):
        self.ask_prices = []
        self.ask_quantity = []
        self.bid_prices = []
        self.bid_quantity = []

        self.bids = []
        self.asks = []

        self.initial_order = []
        self.spred = 0

    @property
    def max_bid(self):
        return max(self.bids) if self.bids else 0

    @property
    def min_ask(self):
        return min(self.asks) if self.asks else float('inf')

    def put_order(self, order):
        if order.side == 0:
            self.bids[order.price].append(order)
        else:
            self.asks[order.price].append(order)

    def delete_order(self, index):
        pass

    def present_orderbook(self):
        pass

class Order:
    def __init__(self, side, price, quantity):
        # first argument: 1 for sell, 0 for buy
        self.side = side
        self.price = price
        self.quantity = quantity

if __name__ == '__main__':
    ob = OrderBook()

    order1 = Order(1, 61.57, 10)
    order2 = Order(0, 57.23, 10)

    ob.initial_order.append(order1)
    ob.put_order(ob.initial_order[0])


class OrderBook:
    def __init__(self):
        self.ask_prices = []
        self.ask_quantity = []
        self.bid_prices = []
        self.bid_quantity = []

    def put_order(self, order):
        pass

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

    Order(0, 12.23, 10)
import pytest
import random
from order_book import *

def random_order():
    core = random.randint(10, 10000)
    remain = random.randint(1, 10)/random.randint(1, 4)
    quantity = random.randint(10, 100)
    return core, remain, quantity

def prepare_data(sells, buys, unique_sells = None, unique_buys = None):
    orders = []
    if not unique_sells:
        unique_sells = sells
    if not unique_buys:
        unique_buys = buys

    k = 0
    core, remain, quantity = random_order()
    for i in range(sells):
        if k < unique_sells:
            core_some, remain, quantity = random_order()
            orders.append(Order(1, core + remain, quantity))
            k += 1
        else:
            orders.append(Order(1, core + remain, quantity))

    k = 0
    for i in range(buys):
        if k < unique_buys:
            core_some, remain, quantity = random_order()
            orders.append(Order(0, core - remain, quantity))
            k += 1
        else:
            orders.append(Order(0, core - remain, quantity))
    return orders

def test_should_be_correct_sorting():
    ob = OrderBook()

    orders = prepare_data(5, 10)

    for order in orders:
        ob.put_order(order)

    ob.present_orderbook()
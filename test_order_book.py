import pytest
import random
from order_book import *

def random_order():
    core = random.randint(10, 10000)
    remain = random.randint(10, 20)/random.randint(10, 30)
    quantity = random.randint(10, 100)
    return core, remain, quantity

def prepare_data(sells, buys, unique_sells = None, unique_buys = None):
    orders = []
    if not unique_sells:
        unique_sells = sells
    if not unique_buys:
        unique_buys = buys

    k = 0
    core, remain_main, quantity = random_order()
    remain = 0
    for i in range(sells):
        if k < unique_sells:
            core_some, remain_again, quantity = random_order()
            orders.append(Order(1, round(core + remain, 1), quantity))
            remain += remain_again
            k += 1
        else:
            orders.append(Order(1, round(core + remain, 1), quantity))

    k = 0
    remain = 0
    for i in range(buys):
        if k < unique_buys:
            core_some, remain_again, quantity = random_order()
            remain += remain_again
            orders.append(Order(0, round(core - remain, 1), quantity))
            k += 1
        else:
            orders.append(Order(0, round(core - remain, 1), quantity))
    return orders

def test_sorting_when_all_price_of_orders_are_different():
    ob = OrderBook()

    orders = prepare_data(5, 10)
    for order in orders:
        ob.put_order(order)
    ob.present_orderbook()

    print("__")
    for order in orders:
        print(order.price)

def test_sorting_when_have_reiterated_price_of_orders():
    pass

def test_get_order():
    pass

def test_delete_order():
    pass

def test_snapshot_market_data():
    pass

def test_market_order():
    pass

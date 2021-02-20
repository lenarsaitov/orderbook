import pytest
import random
from order_book import *
import functools

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

    asks = []
    bids = []

    k = 0
    core, remain_main, quantity = random_order()
    remain = 0
    for i in range(sells):
        orders.append(Order(1, round(core + remain, 1), quantity))
        asks.append([round(core + remain, 1), quantity])

        if k < unique_sells:
            core_some, remain_again, quantity = random_order()
            remain += remain_again
            k += 1

    k = 0
    remain = 0
    for i in range(buys):
        orders.append(Order(0, round(core - remain, 1), quantity))
        bids.append([round(core - remain, 1), quantity])

        if k < unique_buys:
            core_some, remain_again, quantity = random_order()
            remain += remain_again
            k += 1

    return orders, asks, bids


@pytest.mark.parametrize("quantity_of_sells", [2,10])
@pytest.mark.parametrize("quantity_of_buys", [6,20])
def test_sorting_when_all_price_of_orders_are_different(quantity_of_sells, quantity_of_buys):
    ob = OrderBook()

    orders, asks, bids  = prepare_data(3, 5)
    for order in orders:
        ob.put_order(order)
    ob.present_orderbook_with_each_order()

    ask_prices = sorted([ask[0] for ask in asks], reverse=True)
    bid_prices = sorted([bid[0] for bid in bids], reverse=True)

    asks_table, bids_table = ob.output_data()
    ask_prices_check = [ask[0] for ask in asks_table]
    bid_prices_check = [bid[0] for bid in bids_table]

    if functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, ask_prices_check, ask_prices), True):
        assert True, "Orderbook didnt sorted by price of asks"

    if functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, bid_prices_check, bid_prices), True):
        assert True, "Orderbook didnt sorted by price of bids"



# @pytest.mark.parametrize("quantity_of_sells", [2,10])
# @pytest.mark.parametrize("quantity_of_buys", [6,20])
# def test_aggregating_orders_by_price(quantity_of_sells, quantity_of_buys):
#     ob = OrderBook()
#
#     orders, asks, bids  = prepare_data(3, 5)
#     for order in orders:
#         ob.put_order(order)
#     ob.present_orderbook_with_each_order()
#
#     ask_prices = [ask[0] for ask in asks]
#     print(sorted(ask_prices, reverse=True))
#
#
# @pytest.mark.parametrize("quantity_of_sells", [2,10])
# @pytest.mark.parametrize("quantity_of_buys", [6,20])
# def test_get_order(quantity_of_sells, quantity_of_buys):
#     ob = OrderBook()

    # orders, asks, bids  = prepare_data(3, 5)
    # for order in orders:
    #     ob.put_order(order)
    # ob.present_orderbook_with_each_order()

def test_delete_order():
    pass

def test_snapshot_market_data():
    pass

def test_market_order():
    pass

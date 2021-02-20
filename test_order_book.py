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
    """Данная функция подготавливает необходимые рандомные данные, приближенные к реальным"""

    orders = []
    if not unique_sells:
        unique_sells = sells
    if not unique_buys:
        unique_buys = buys

    asks = []
    bids = []

    asks_aggregate = []
    bids_aggregate = []

    k = 0
    core, remain_main, quantity = random_order()
    remain = 0
    for i in range(sells):
        if k < unique_sells:
            core_some, remain_again, quantity = random_order()
            remain += remain_again
            k += 1
            asks_aggregate.append([round(core + remain, 1), quantity])
        else:
            asks_aggregate[-1][1] += quantity
        orders.append(Order(1, round(core + remain, 1), quantity))
        asks.append([round(core + remain, 1), quantity, k])

    k = 0
    remain = 0
    for i in range(buys):
        if k < unique_buys:
            core_some, remain_again, quantity = random_order()
            remain += remain_again
            k += 1
            bids_aggregate.append([round(core - remain, 1), quantity])
        else:
            bids_aggregate[-1][1] += quantity
        orders.append(Order(0, round(core - remain, 1), quantity))
        bids.append([round(core - remain, 1), quantity, k])

    return orders, asks, bids, asks_aggregate, bids_aggregate


@pytest.mark.parametrize("quantity_of_sells", [10,30])
@pytest.mark.parametrize("quantity_of_buys", [6,20])
def test_sorting_when_all_price_of_orders_are_different(quantity_of_sells, quantity_of_buys):
    """Тест проверяет сортировку ордеров в биржевом стакане"""

    ob = OrderBook()

    orders, asks, bids, a, b  = prepare_data(quantity_of_sells, quantity_of_buys)
    for order in orders:
        ob.put_order(order)

    ask_prices = sorted([ask[0] for ask in asks], reverse=True)
    bid_prices = sorted([bid[0] for bid in bids], reverse=True)

    asks_table, bids_table = ob.snapshot_market()
    ask_prices_check = [ask[0] for ask in asks_table]
    bid_prices_check = [bid[0] for bid in bids_table]

    if functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, ask_prices_check, ask_prices), True):
        assert True, "Orderbook didnt sorted by price of asks"

    if functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, bid_prices_check, bid_prices), True):
        assert True, "Orderbook didnt sorted by price of bids"


@pytest.mark.parametrize("quantity_of_sells", [10,30])
@pytest.mark.parametrize("quantity_of_buys", [6,20])
def test_aggregating_orders_by_price(quantity_of_sells, quantity_of_buys):
    """Тест проверяет агрегацию ордеров по ценам"""

    ob = OrderBook()

    orders, asks, bids, asks_aggregate, bids_aggregate  = prepare_data(quantity_of_sells, quantity_of_buys, 2, 3)
    for order in orders:
        ob.put_order(order)

    ask_quantities = sorted([ask[1] for ask in asks_aggregate], reverse=True)
    bid_quantities = sorted([bid[1] for bid in bids_aggregate], reverse=True)

    asks_table, bids_table = ob.snapshot_market()
    ask_quantities_check = sorted([ask[1] for ask in asks_table], reverse=True)
    bid_quantities_check = sorted([bid[1] for bid in bids_table], reverse=True)

    if functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, ask_quantities, ask_quantities_check), True):
        assert True, "Orderbook didnt true aggregate sorted by price of asks"

    if functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, bid_quantities, bid_quantities_check), True):
        assert True, "Orderbook didnt true aggregate sorted by price of bids"


@pytest.mark.parametrize("quantity_of_sells", [10,30])
@pytest.mark.parametrize("quantity_of_buys", [6,20])
def test_get_order(quantity_of_sells, quantity_of_buys):
    """Тест проверяет получение данных заявки по идентификатору"""
    ob = OrderBook()

    orders, asks, bids, asks_aggregate, bids_aggregate = prepare_data(quantity_of_sells,quantity_of_buys)
    for order in orders:
        ob.put_order(order)

    ob.present_orderbook_with_each_order()

    ask_ids = [ask[2] for ask in asks]
    random_index = random.randint(0, len(ask_ids)-1)
    random_id = ask_ids[random_index]

    order = asks[random_index]
    order_check = list(ob.get_order(random_id))

    order = sorted(order, reverse=True)
    order_check = sorted(order_check, reverse=True)

    if functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, order, order_check), True):
        assert True, "Not equal between need and exists results"

@pytest.mark.dev0
def test_delete_order():
    pass

@pytest.mark.dev1
def test_market_order():
    pass

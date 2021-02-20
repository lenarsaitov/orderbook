### Биржевой стакан на Python

*Задание*: реализовать биржевой стакан на Python

#### Методы и сущности
В данной работе фигурируют две сущности: это биржевой стакан OrderBook и заявка Order

Реализованные методы класса OrderBook
* Постановка заявки в стакан (put_order)
* Снятие заявки по идентификатору заявки (delete_order)
* Получение данных заявки по идентификатору (get_order)
* Получение снапшота рыночных данных с необходимой агрегацией и сортировкой по цене (snapshot_market) 
* Вывод в консоль заявок с сортировкой по цене (present_orderbook_with_each_order)

Класс заявой Order имеет следующие свойства:
* Side. Сторона торговли. 0 если покупатель, 1 если продавец
* Price. Цена товара
* Quantity. Количество товара  

Также реализованы тесты:
* Проверка сортировки ордеров в биржевом стакане
* Проверка агрегации ордеров по ценам
* Проверка получения данных заявки по идентификатору

Тесты рекомендуется запускать командой:
pytest -v --tb=line test_order_book.py

P.S. В связи ограничением по времени выполнения задания проекте пока не реализован механизм рыночного ордера и лимитный ордер Stop Loss
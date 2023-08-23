"""
Зависимость
"""
import time


class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Order:
    def __init__(self, *products) -> None:
        self.products: list[Product] = list(products)
    
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total


class PaymentProcessor:
    def process_payment(self, order: Order):
        total_price = order.calculate_total()
        """
        логика оплаты
        """
        time.sleep(1.5)
        print('Success. Total cost:', total_price)

pr1 = Product("Ball", 4000)
pr2 = Product("Book", 6000)
order = Order(pr1, pr2)

payment_processor = PaymentProcessor()
payment_processor.process_payment(order)
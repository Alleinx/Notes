from abc import ABC, abstractmethod

class Customer:
    """Defines customer's properties"""
    def __init__(self, name, fidelity):    
        self.name = name
        self.fidelity = fidelity

class LineItem:
    """Defines item's properties"""
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def cal_discount(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        
        return self.total() - discount

    def __repr__(self):
        return '<Original price: {0}, total price: {1}>'.format(self.total(), self.cal_discount())

class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """Returns discount amount"""
    

class FidelityPromo(Promotion):

    def discount(self, order):
        if order.customer.fidelity >= 1000:
            return order.total() * 0.05
        else:
            return 0

class BulkItemPromo(Promotion):

    def discount(self, order: Order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.01

        return discount

class LargeOrderPromo(Promotion):

    def discount(self, order: Order):
        distinct_item = {item.product for item in order.cart}

        if len(distinct_item) >= 10:
            return order.total() * 0.07

        return 0

if __name__ == "__main__":
    joe = Customer('John Doe', 0)
    ana = Customer('Ana', 1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0),
    ]

    print(Order(joe, cart, promotion=FidelityPromo()))
    print(Order(ana, cart, promotion=FidelityPromo()))

    cart = [
        LineItem('banana', 40, .5),
        LineItem('apple', 30, 1.5),
        LineItem('watermellon', 50, 5.0),
    ]
    print(Order(joe, cart, promotion=BulkItemPromo()))
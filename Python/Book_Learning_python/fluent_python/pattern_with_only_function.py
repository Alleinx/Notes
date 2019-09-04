from pattern import Customer, LineItem

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        
        return self.total() - discount

    def __repr__(self):
        return '<Order total: {0} due: {1}'.format(self.total(), self.due())

def fidelity_promo(order: Order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order: Order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.01
    
    return discount
    
if __name__ == "__main__":
    joe = Customer('John Doe', 0)
    ana = Customer('Ana', 1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0),
    ]

    print(Order(joe, cart, promotion=fidelity_promo))
    print(Order(ana, cart, promotion=fidelity_promo))

    cart = [
        LineItem('banana', 40, .5),
        LineItem('apple', 30, 1.5),
        LineItem('watermellon', 50, 5.0),
    ]
    print(Order(joe, cart, promotion=bulk_item_promo))
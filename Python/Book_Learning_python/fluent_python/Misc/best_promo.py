from pattern import Customer, LineItem
import inspect
import promotions

# Put all promo methods in promotions.py into a list:
promos = [func for name, func in
            inspect.getmembers(promotions, inspect.isfunction)]

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

def best_promo(order):
    """Choose the best promotion for different customer"""
    return max(promo(order) for promo in promos)

    
if __name__ == "__main__":
    joe = Customer('John Doe', 0)
    ana = Customer('Ana', 1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0),
    ]

    print(Order(joe, cart, promotion=best_promo))
    print(Order(ana, cart, promotion=best_promo))

    cart = [
        LineItem('banana', 40, .5),
        LineItem('apple', 30, 1.5),
        LineItem('watermellon', 50, 5.0),
    ]
    
    print(Order(joe, cart, promotion=best_promo))
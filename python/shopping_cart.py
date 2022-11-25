from abc import ABC, abstractmethod
from typing import Dict

from shopping_cart_interface import IShoppingCart
from pricer import Pricer
from formatter_interface import Formatter

class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """
    def __init__(self, pricer: Pricer,formater:Formatter):
        self.pricer = pricer
        self._contents = []
        self.formater = formater
        

    def add_item(self, item_type: str, number: int):
        # adds new item to or update existing item in the shopping cart
        # if item_type not in self._contents:
        #     self._contents[item_type] = number
        # else:
        #     self._contents[item_type] = self._contents[item_type] + number
        self._contents.append((item_type,number)) 
        # every time an item is scanned it is added onto the end of the list 
        # then the list is printed in order

    def print_receipt(self):
        total = 0
        for index in range(len(self._contents)):
            (key,value) = self._contents[index]
            price = self.pricer.get_price(key)
            total = total + price*value
            print(self.formater.format_items(key,value,price))
        print(self.formater.format_total(total))

class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """
    @abstractmethod
    def factory_method(self,formatter:Formatter) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self,formatter:Formatter) -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        return self.factory_method(formatter)

class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """
    def factory_method(self,formatter) -> ShoppingCart:
        # returns ShoppingCart object
        return ShoppingCart(Pricer(),formatter)

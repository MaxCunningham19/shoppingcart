import unittest

from shopping_cart import ShoppingCartConcreteCreator, ShoppingCart
from test_utils import Capturing, BasicFormatter, PriceFirstFormatter


TOTAL = "total"
class ShoppingCartTest(unittest.TestCase):
    def perform(self,operations,formatter):
        '''
        operations : [
            (key, amount, expected_outcome),
            ..
            ..
            ..
            (TOTAL,NA,expected_total)
        ]
        formatter : class Formatter (formatter.py)
        '''
        sc = ShoppingCartConcreteCreator().operation(formatter)
        for (key, amount,_) in operations:
            if key is not TOTAL:
                sc.add_item(key, amount)
        with Capturing() as output:
            sc.print_receipt()
        for i in range(len(operations)):
            (_, _, expected_outcome) = operations[i]
            self.assertEqual(expected_outcome, output[i])

    def test_print_receipt(self):
        operations = [
            ("apple", 2, "apple - 2 - 100"),
            (TOTAL,0,"Total - 200")
        ]
        self.perform(operations,BasicFormatter())

    def test_doesnt_explode_on_mystery_item(self):
        operations = [
            ("apple", 2, "apple - 2 - 100"),
            ("banana", 5, "banana - 5 - 200"),
            ("pear", 5, "pear - 5 - 0"),
            (TOTAL,0,"Total - 1200")
        ]
        self.perform(operations,BasicFormatter())

    def test_item_printed_in_order(self):
        operations = [
            ("banana", 5, "banana - 5 - 200"),
            ("apple", 2, "apple - 2 - 100"),
            ("pear", 5, "pear - 5 - 0"),
            (TOTAL,0,"Total - 1200")
        ]
        self.perform(operations,BasicFormatter())

    def test_formatting_works(self):
        operations = [
            ("banana", 5, "200 - 5 - banana"),
            ("apple", 2, "100 - 2 - apple"),
            ("pear", 5, "0 - 5 - pear"),
            (TOTAL,0,"Total - 1200")
        ]
        self.perform(operations,PriceFirstFormatter())

unittest.main(exit=False)

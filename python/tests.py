import unittest

from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing, BasicFormatter, PriceFirstFormatter


class ShoppingCartTest(unittest.TestCase):
    def test_print_receipt(self):
        sc = ShoppingCartConcreteCreator().operation(BasicFormatter())
        sc.add_item("apple", 2)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple - 2 - 100", output[0])
        self.assertEqual("Total - 200", output[1])

    def test_doesnt_explode_on_mystery_item(self):
        sc = ShoppingCartConcreteCreator().operation(BasicFormatter())
        sc.add_item("apple", 2)
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple - 2 - 100", output[0])
        self.assertEqual("banana - 5 - 200", output[1])
        self.assertEqual("pear - 5 - 0", output[2])
        self.assertEqual("Total - 1200",output[3])

    def test_item_printed_in_order(self):
        sc = ShoppingCartConcreteCreator().operation(BasicFormatter())
        sc.add_item("banana", 5)
        sc.add_item("apple", 2)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("banana - 5 - 200",output[0])
        self.assertEqual("apple - 2 - 100",  output[1])
        self.assertEqual("pear - 5 - 0", output[2])
        self.assertEqual("Total - 1200",output[3])

    def test_formatting_works(self):
        sc = ShoppingCartConcreteCreator().operation(PriceFirstFormatter())
        sc.add_item("banana", 5)
        sc.add_item("apple", 2)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("200 - 5 - banana",output[0])
        self.assertEqual("100 - 2 - apple",  output[1])
        self.assertEqual("0 - 5 - pear", output[2])
        self.assertEqual("Total - 1200",output[3])

unittest.main(exit=False)

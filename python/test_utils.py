from io import StringIO
import sys
from shopping_cart import Formatter
class Capturing(list):
    """ Helper for capturing the output receipts"""
    _stdout = None
    _stringio = None

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

class BasicFormatter(Formatter):
    def __init__(self) -> None:
        return 

    def format_items(self,key,value,price)->str:
        return f"{key} - {value} - {price}"

    def format_total(self,total)->str:
        return f"Total - {total}"

class PriceFirstFormatter(Formatter):
    def __init__(self) -> None:
        return 

    def format_items(self,key,value,price)->str:
        return f"{price} - {value} - {key}"

    def format_total(self,total)->str:
        return f"Total - {total}"

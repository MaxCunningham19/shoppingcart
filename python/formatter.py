from abc import ABC

class Formatter(ABC):
    """
    Interface used to define the function to format printing.
    """
    def format_items(self,key,value,price)->str:
        # needs to return a string containing some combination of key value and price
        pass

    def format_total(self,total)->str:
        # needs to return a string containg the total
        pass

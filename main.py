# main.py

from product_manager import ProductManager
from product import Product
import random

def main():
    manager = ProductManager()

    manager.add_product(Product("MacBook", 1200.99, 5))
    manager.add_product(Product("Monitor2", 25.50, 15))
    manager.add_product(Product("Mechanic Keyboard", 45.00, 10))
    
       
    
if __name__ == "__main__":
    main()

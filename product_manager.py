# product_manager.py

from product import Product 

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product.display_info())

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value

# Primer korišćenja
if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product("Laptop", 1000, 5)
    manager.add_product("Telefon", 500, 10)
    manager.display_all_products()
    manager.totatotal_inventory_value()  



    def remove_product_by_name(self, name):
        """Uklanja proizvod sa zadatim imenom, ako postoji."""
        self.products = [p for p in self.products if p.name != name]

# Primer korišćenja:
# manager = ProductManager()
# manager.add_product(Product("Laptop", 1000))
# manager.remove_product_by_name("Laptop")

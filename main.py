from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Monitor", 200, 4)
p2 = Product("Web kamera", 80, 6)
p3 = Product("Slušalice", 120, 2)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

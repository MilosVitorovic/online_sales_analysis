from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

p1 = Product("Monitor", 200, 4)
p2 = Product("Web kamera", 80, 6)
p3 = Product("Slušalice", 120, 2)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

cart = Cart()

cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

cart.show_cart()
print("Ukupno za naplatu:", cart.total_cart_value())

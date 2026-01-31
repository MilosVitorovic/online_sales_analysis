from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

p1 = Product("Laptop", 1000, 3)
p2 = Product("Miš", 20, 10)
p3 = Product("Tastatura", 50, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

cart = Cart()

cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

cart.show_cart()
print("Ukupno za naplatu:", cart.total_cart_value())

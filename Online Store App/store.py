from cart import Cart 
class Store:
    def __init__(self):
        self.products = {}
        self.cart = Cart() 

    def add_product_to_store(self, product):
        if product.id in self.products:
            raise ValueError("Duplicate ID — this product is already registered")
        else:
            self.products[product.id] = product

    def remove_product_from_store(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product not found in store.")
        if product_id in self.cart.products:
            del self.cart.products[product_id]
        del self.products[product_id]

    def find_product_by_id(self, product_id):
        return self.products.get(product_id)

    def get_all_products(self):
        return list(self.products.values())  
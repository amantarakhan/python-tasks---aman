class Cart:
    def __init__(self):
        self.products = {}
        # a dictionary -> we use the product id as a key -> {'product': product, 'quantity': quantity} as a value

    def add_product_to_cart(self, product, quantity):
        if quantity > 0:
            if product.id in self.products:
                self.products[product.id]['quantity'] += quantity
            else:
                self.products[product.id] = {'product': product, 'quantity': quantity}
        else:
            raise ValueError("Quantity must be more than 0")

    def remove_product_from_cart(self, product, quantity):
        if quantity > 0:
            if product.id in self.products:
                self.products[product.id]['quantity'] -= quantity
                if self.products[product.id]['quantity'] <= 0:
                    del self.products[product.id]
            else:
                raise ValueError("You don't have this product in your cart")
        else:
            raise ValueError("Quantity must be more than 0")

    def calculate_total_price(self):
        total_price = 0
        for p in self.products.values():
            total_price += p['product'].get_price() * p['quantity']
        return total_price

    def clear_cart(self):
        self.products.clear()
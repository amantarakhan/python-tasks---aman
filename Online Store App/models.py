# --------- the super class ----------------
class Product:
    def __init__(self, id, name, base_price):
        self.id = id
        self.name = name
        if base_price >= 0:
            self.base_price = base_price
        else:
            raise ValueError("Price cannot be negative")

    def get_price(self):
        return self.base_price

    def get_details(self):
        return f"{type(self).__name__}: {self.name} (ID: {self.id}) - ${self.get_price():.2f}"

# --------- the sub classes ----------------

class PhysicalProduct(Product):
    def __init__(self, id, name, base_price, shipping_cost):
        super().__init__(id, name, base_price)
        if shipping_cost >= 0:
            self.shipping_cost = shipping_cost
        else:
            raise ValueError("Shipping cost cannot be negative")

    def get_price(self):
        return self.base_price + self.shipping_cost


class DigitalProduct(Product):
    def __init__(self, id, name, base_price):
        super().__init__(id, name, base_price)


class DiscountedProduct(Product):
    def __init__(self, id, name, base_price, discount_percentage):
        super().__init__(id, name, base_price)
        if 0 <= discount_percentage <= 100:
            self.discount_percentage = discount_percentage
        else:
            raise ValueError("Discount must be between 0 and 100")

    def get_price(self):
        return self.base_price * (1 - self.discount_percentage / 100)


class SubscriptionProduct(Product):
    def __init__(self, id, name, base_price, duration_in_months, monthly_fee):
        super().__init__(id, name, base_price)

        if duration_in_months > 0:
            self.duration_in_months = duration_in_months
        else:
            raise ValueError("Duration must be a positive value")

        if monthly_fee > 0:
            self.monthly_fee = monthly_fee
        else:
            raise ValueError("Monthly fee must be a positive value")

    def get_price(self):
        return self.duration_in_months * self.monthly_fee

# this is the parent class that we will use it later in inheritance 
class Product : 
    def __init__ (self , product_id , name , base_price ) : 
        self.product_id = product_id 
        self.name = name 
        self.base_price = float(base_price)

    def __str__ (self) : #this return a string -> so when we print any object it have a decent format 
        return f"Product: {self.name} (ID: {self.product_id}) - ${self.base_price:.2f}"

    def calculate_final_price(self) : 
        return self.base_price 
    



#---------Children classes ---------------
class ElectronicProduct(Product):
    def __init__(self, product_id, name, base_price, warranty_months):
        # We take ALL arguments
        super().__init__(product_id, name, base_price)
        # We keep the one that is specific to this child
        self.warranty_months = warranty_months

    def __str__(self):
        return super().__str__() + f" | Warranty: {self.warranty_months} months"

    def calculate_final_price(self):
        return self.base_price * 1.10

class PerishableProduct(Product):
    def __init__(self, product_id, name, base_price, days_until_expiry):
        super().__init__(product_id, name, base_price)
        self.days_until_expiry = days_until_expiry

    def __str__(self):
        return super().__str__() + f" | Expires in: {self.days_until_expiry} days"

    def calculate_final_price(self):
        if self.days_until_expiry < 7:
            # 50% discount
            return self.base_price * 0.50
        return self.base_price
    
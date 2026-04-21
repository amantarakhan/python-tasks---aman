
#---- the manager class -------------------
class Warehouse : 
    def __init__ (self) : 
        self.products = [] 
    
    def add_product ( self , product ) :
        self.products.append(product)

    def display_inventory(self) : 
        for p in self.products : 
            print(p) 
    
    def get_total_value (self) : 
        total_price = 0 
        for p in self.products : 
            total_price += p.calculate_final_price()
        return total_price

            


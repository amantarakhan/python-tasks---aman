
from models import PerishableProduct , ElectronicProduct
from warehouse import Warehouse

def main() : 
    my_warehouse = Warehouse() 

    laptop = ElectronicProduct("E101", "Gaming Laptop", 1000, 24)
    milk_fresh = PerishableProduct("P202", "Fresh Milk", 10.0, 10)
    milk_old = PerishableProduct("P203", "Expiring Milk", 10.0, 3)

    my_warehouse.add_product(laptop)   
    my_warehouse.add_product(milk_fresh) 
    my_warehouse.add_product(milk_old) 

    my_warehouse.display_inventory() 

    total = my_warehouse.get_total_value()

    print("\n" + "="*30)
    print(f"Total Warehouse Value: ${total:.2f}")
    print("="*30)

if __name__ == "__main__":
    main()


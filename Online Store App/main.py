from store import Store
from models import PhysicalProduct, DigitalProduct, DiscountedProduct, SubscriptionProduct


# helper function to validate the user input 
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def get_valid_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def main():
    my_store = Store()

    while True:
        print("""
---------------------------------
      ONLINE STORE MANAGER
---------------------------------
1.  Add New Product to Store
2.  Display All Products
3.  Search Product by ID
4.  Add Product to Cart
5.  Remove Product from Cart
6.  View Cart Contents
7.  View Total Price
8.  Clear Cart
9.  Remove Product from Store
10. Exit
---------------------------------
        """)

        choice = get_valid_int("Select an option (1-10): ")

        try:
            match choice:
                case 1:  # Add New Product to Store
                    print("\nSelect Type: 1.Physical  2.Digital  3.Discounted  4.Subscription")
                    ptype = get_valid_int("Choice: ")

                    pid = get_valid_string("ID: ")
                    name = get_valid_string("Name: ")
                    price = float(input("Base Price: "))

                    match ptype:
                        case 1:
                            ship = float(input("Shipping Cost: "))
                            product = PhysicalProduct(pid, name, price, ship)
                        case 2:
                            product = DigitalProduct(pid, name, price)  # ✅ Fixed: was printing products list here
                        case 3:
                            disc = float(input("Discount %: "))
                            product = DiscountedProduct(pid, name, price, disc)
                        case 4:
                            dur = get_valid_int("Duration (Months): ")
                            fee = float(input("Monthly Fee: "))
                            product = SubscriptionProduct(pid, name, price, dur, fee)
                        case _:
                            print("Invalid product type.")
                            continue

                    my_store.add_product_to_store(product)
                    print("Product added to store!")

                case 2:  # Display All Products
                    products = my_store.get_all_products()
                    if not products:
                        print("The store is empty.")
                    else:
                        for p in products:
                            print(p.get_details())  # ✅ Fixed: was print(p) which showed object reference

                case 3:  # Search for Product by ID
                    pid = get_valid_string("Enter ID to search: ")
                    product = my_store.find_product_by_id(pid)
                    if product:
                        print(f"Found: {product.get_details()}")
                    else:
                        print("Product not found.")

                case 4:  # Add Product to Cart
                    pid = get_valid_string("Product ID: ")
                    product = my_store.find_product_by_id(pid)
                    if product:
                        qty = get_valid_int("Quantity: ")
                        my_store.cart.add_product_to_cart(product, qty)  # ✅ Fixed: was add_profuct_to_cart
                        print("Added to cart.")
                    else:
                        print("Product doesn't exist in store.")

                case 5:  # Remove from Cart
                    pid = get_valid_string("Product ID: ")
                    product = my_store.find_product_by_id(pid)
                    if product:
                        qty = get_valid_int("Quantity to remove: ")
                        my_store.cart.remove_product_from_cart(product, qty)  # ✅ Fixed: was remove_profuct_from_cart
                        print("Cart updated.")
                    else:
                        print("Product doesn't exist in store.")

                case 6:  # View Cart Contents
                    if not my_store.cart.products:
                        print("Your cart is empty.")
                    else:
                        print("\n--- Cart Contents ---")
                        for data in my_store.cart.products.values():
                            p, q = data['product'], data['quantity']
                            print(f"- {p.name} (x{q}): ${p.get_price() * q:.2f}")

                case 7:  # View Total Price
                    if not my_store.cart.products:
                        print("Your cart is empty.")
                    else:
                        for data in my_store.cart.products.values():
                            p, q = data['product'], data['quantity']
                            print(f"- {p.name} (x{q}): ${p.get_price() * q:.2f}")
                        total = my_store.cart.calculate_total_price()
                        print(f"\nGRAND TOTAL: ${total:.2f}")

                case 8:  # Clear Cart
                    my_store.cart.clear_cart()
                    print("Cart cleared.")

                case 9:  # Remove Product from Store
                    pid = get_valid_string("Enter Product ID to remove from store: ")
                    my_store.remove_product_from_store(pid)
                    print("Product removed from store.")

                case 10:  # Exit
                    print("Goodbye!")
                    break

                case _:
                    print("Invalid option. Please select 1-10.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
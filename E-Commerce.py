# Simple E-commerce Application

products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Smartphone", "price": 20000},
    3: {"name": "Headphones", "price": 1500},
    4: {"name": "Keyboard", "price": 800},
    5: {"name": "Mouse", "price": 500}
}

cart = {}

def display_products():
    print("\nAvailable Products:")
    for pid, info in products.items():
        print(f"{pid}. {info['name']} - ₹{info['price']}")

def add_to_cart():
    try:
        product_id = int(input("Enter Product ID to add to cart: "))
        if product_id in products:
            quantity = int(input("Enter quantity: "))
            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity
            print(f"{products[product_id]['name']} added to cart.")
        else:
            print("Invalid Product ID.")
    except ValueError:
        print("Please enter valid numbers.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("\n🛒 Your Cart:")
    total = 0
    for pid, qty in cart.items():
        name = products[pid]['name']
        price = products[pid]['price']
        cost = qty * price
        total += cost
        print(f"{name} x {qty} = ₹{cost}")
    print(f"Total: ₹{total}")

def checkout():
    if not cart:
        print("Your cart is empty. Add items first.")
        return
    view_cart()
    confirm = input("Do you want to place the order? (yes/no): ").lower()
    if confirm == 'yes':
        print("🎉 Order placed successfully!")
        cart.clear()
    else:
        print("Order cancelled.")

def main():
    while True:
        print("\n---- E-Commerce Menu ----")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            display_products()
        elif choice == '2':
            display_products()
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Try again.")

main()

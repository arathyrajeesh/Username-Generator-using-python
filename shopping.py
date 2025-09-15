shop_items = [
    {
        "order_id" : 1,
        "name" : "Laptop",
        "price" : 57000
    },
    {
        "order_id" : 2,
        "name" : "KeyBoard",
        "price" : 3000
    },
    {
        "order_id" : 3,
        "name" : "Mouse",
        "price" : 900
    }
]
cart = []
def show_items():
    print("Shopping List\n")
    for i in shop_items:
        print(f"{i['order_id']}.{i['name']} - ₹{i['price']}")
def add_items():
    show_items()
    input_id = int(input("Enter the id for add to cart: "))
    for i in shop_items:
        if i['order_id'] == input_id:
            cart.append(i)
            print(f"{i['name']} added to cart")
            return
    print("Enter valid order id")
def remove_items():
    view_cart()
    input_id = int(input("Enter the id for remove from cart"))
    for i in cart:
        if i['order_id'] == input_id:
            cart.remove(i)
            print(f"{i['name']} removed from cart")
            return
    print("Enter valid order id")
def view_cart():
    total = 0
    if not cart:
        print("Your Cart is Empty!!")
    else:
        for i in range(len(cart)):
            item = cart[i]
            print(f"{i+1}.{item['name']} - ₹{item['price']}")            
            total += item['price']
        print(f"Total Price ₹{total}")
def shopping_cart():
    while True:
        print("\nShopping Cart System")
        print("1.Show Items")
        print("2.Add Items")
        print("3.Remove Items")
        print("4.View Total")
        print("5.Exit")        
        choice = int(input("Enter the choice: "))        
        if choice == 1:
            show_items()
        elif choice == 2:
            add_items()
        elif choice == 3:
            remove_items()
        elif choice == 4:
            view_cart()
        elif choice == 5:
            print("Exiting from shopping cart system")
            break
        else:
            print("Invalid Choice")
shopping_cart()
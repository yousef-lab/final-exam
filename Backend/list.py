products = [
    {"name": "Product 1", "price": 100},
    {"name": "Product 2", "price": 200},
    {"name": "Product 3", "price": 150},
    {"name": "Product 4", "price": 300},
    {"name": "Product 5", "price": 250}
]

while True:
    print("\nProducts List:")
    print("1. Product 1 - 100 SAR")
    print("2. Product 2 - 200 SAR")
    print("3. Product 3 - 150 SAR")
    print("4. Product 4 - 300 SAR")
    print("5. Product 5 - 250 SAR")
    print("0. Exit")

    num = input("Enter product number: ")

    if num == "0":
        break

    try:
        num = int(num)
        
        if num == 1:
            price = 100
        elif num == 2:
            price = 200
        elif num == 3:
            price = 150
        elif num == 4:
            price = 300
        elif num == 5:
            price = 250
        else:
            print("Error: Invalid product number!")
            continue

        tax = price * 0.15
        total = price + tax

        print("\nProduct: Product " + str(num))
        print("Original Price: " + str(price) + " SAR")
        print("Tax (15%): " + str(round(tax, 2)) + " SAR")
        print("Total Price: " + str(round(total, 2)) + " SAR")

    except:
        print("Error: Please enter numbers only!")

#Assessment 2 - Jack Petrie

# Function to get 5 products and prices from the user
def get_products():
    products = []
    for i in range(5):
        name = input("Enter product name: ")
        price = float(input("Enter price: £"))
        products.append([name, price])
    return products

# Function to get the price value (sorting)
def get_price(item):
    return item[1]

# Function to sort products from highest to lowest
def sort_products(products):
    products.sort(key=get_price, reverse=True)
    return products

# Function to calculate total and apply discount
def calculate_total(products):
    total = 0
    for item in products:
        total += item[1]
    cheapest = products[-1]
    total_owed = total - cheapest[1]
    return total_owed, cheapest

# Function to display the results
def display_results(products, cheapest, total_owed):
    print("\nProducts sorted by price (highest to lowest):")
    for item in products:
        print(item[0], "£", item[1])

    print("\nFree item:", cheapest[0])
    print("Total owed: £", total_owed) 
    
# Run the program
products = get_products()
products = sort_products(products)
total_owed, cheapest = calculate_total(products)
display_results(products, cheapest, total_owed)
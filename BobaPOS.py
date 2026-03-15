base_price = {
    "classic": 4.50,
    "honey": 5.00,
    "thai": 5.00,
    "jasmine": 5.25,
    "taro": 5.25
}

size_price = {
    "small": 0,
    "medium": 0.25,
    "large": 0.5,
    "mega": 1
}

top_price = {
    "black tapioca": 0.25,
    "white tapioca": 0.25,
    "egg pudding": 0.75,
    "jelly pearl": 0.5,
    "milk foam": 0.75
}


# The procedure take in a list of orders and total cost, and print the receipt
def print_receipt(order, total):
    print("""
Here is your receipt:
""")
    for item in order:
        if item in base_price:
            itemF = item.capitalize() + " Milk Tea"
            print(f"{itemF:<20} ${base_price[item]:.2f}")

        elif item in size_price:
            itemF = item.capitalize() + " Size"
            print(f"{itemF:<20} ${size_price[item]:.2f}")

        else:
            itemF = item.capitalize()
            print(f"{itemF:<20} ${top_price[item]:.2f}")
    print("-------------------------")
    print(f"{'Total:':<20} ${total}")
    
####################################################
################## MAIN PROGRAM ####################

order_list = [] 
total = 0
print("Welcome to the Virtual MilkT!")


# Print MT menu, get MT selection
print("""
Milk Teas""")

for base in base_price:
    baseF = base.capitalize()
    print(f"{baseF:<20} ${base_price[base]:.2f}")

while(True):
    try:
        choice = input("""
Please enter your selection: """).lower()
        total += base_price[choice]
        order_list.append(choice)
        break
    except KeyError: 
        print("Invalid input. Item not found in menu, please try again.")
        


# Print Size menu, get Size selection
print("""
Drink Sizes""")

for size in size_price:
    sizeF = size.capitalize()
    print(f"{sizeF:<19} +${size_price[size]:.2f}")

while(True):
    try:
        choice = input("""
Please enter your selection: """).lower()
        total += size_price[choice]
        order_list.append(choice)
        break
    except KeyError: 
        print("Invalid input. Item not found in menu, please try again.")


# Print Topping menu, get Topping selection
print("""
Toppings""")

for top in top_price:
    topF = top.capitalize()
    print(f"{topF:<19} +${top_price[top]:.2f}")
print("")

while(True):
    try:
        while(True):
            choice = input("""Please enter your selection (type 0 to finish): """).lower()
            if choice == "0":
                break
            total += top_price[choice]
            order_list.append(choice)
        break
    except KeyError: 
        print("Invalid input. Item not found in menu, please try again.")

print_receipt(order_list, total)
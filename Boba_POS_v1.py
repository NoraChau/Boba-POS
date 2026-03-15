mt = ['Classic', 'Honey', 'Thai', 'Jasmine', 'Taro']
mtPrice = [4.50, 5.00, 5.00, 5.25, 5.25]

top = ['Black Tapioca', 'White Tapioca', 'Egg Pudding', 'Jelly Pearl', "Milk Foam"]
topPrice = [.25, .25, .75, .5, .75]

s = ['Small', 'Medium', 'Large', 'Mega']
sPrice = [0, .25, .5, 1]

order_list = []

"""
The procedure take in a list of orders, calculate the total price, and print the receipt
"""
def print_receipt(order):
    # Calculate total
    total = 0
    for i in range(len(order)):
        if order[i][0] == 'mt':
            total += mtPrice[order[i][1]-1]
        elif order[i][0] == 'top':
            total += topPrice[order[i][1]-1]
        else:
            total += sPrice[order[i][1]-1]
    
    # Receipt
    print("""
Here is your receipt:
""")
    for i in range(len(order)):
        if order[i][0] == 'mt':
            print(f"{mt[order[i][1]-1]} Milk Tea     ${mtPrice[order[i][1]-1]}")
        elif order[i][0] == 'top':
            print(f"{top[order[i][1]-1]}     ${topPrice[order[i][1]-1]}")
        else:
            print(f"{s[order[i][1]-1]} Size         ${sPrice[order[i][1]-1]}")
    print("-------------------------")
    print(f"Total:          ${total}")

######################################

print("Welcome to the Virtual MilkT. I'm Bobot (short for Boba Robot), and I will be your assistant today.")

# Print MT menu, get MT selection
print("""
Milk Teas""")
for i in range(len(mt)):
    print(f"{i+1}. {mt[i]} Milk Tea    ${mtPrice[i]}")
order_list.append(['mt', int(input("""
Please enter the number of your selection: """))])

# Print Size menu, get Size selection
print("""
Drink Sizes""")
for i in range(len(s)):
    print(f"{i+1}. {s[i]}     +${sPrice[i]}")
order_list.append(['s', int(input("""
Please enter the number of your selection: """))])

# Print Topping menu, get Topping selection
print("""
Toppings""")
for i in range(len(top)):
    print(f"{i+1}. {top[i]}     ${topPrice[i]}")
print("")
while True:
    choice = int(input("""Please enter the number of your selection (0 to STOP): """))
    if choice == 0:
        break
    else:
        order_list.append(['top', choice])

print_receipt(order_list)

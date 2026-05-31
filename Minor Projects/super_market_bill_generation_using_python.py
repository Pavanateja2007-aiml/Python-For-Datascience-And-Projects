from datetime import datetime

name = input("Enter Customer Name: ")

# List of items
lists = '''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/liter
Paneer  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/kg
Colgate Rs 85/kg
'''
print(lists)

# Initialize variables
price = 0
pricelist = []
totalprice = 0
finalamount = 0
quantitylist = []
itemlist = []

# Rates for items
items = {
    'rice': 20,
    'sugar': 30,
    'salt': 20,
    'oil': 80,
    'paneer': 110,
    'maggi': 50,
    'boost': 90,
    'colgate': 85
}

option = int(input("For list of items press 1: "))
if option == 1:
    print(lists)

for i in range(len(items)):
    inp1 = int(input("If you want to buy press 1 or 2 for exit: "))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter Your Item: ").lower()
        quantity = int(input("Enter your quantity: "))
        if item in items.keys():
            price = quantity * items[item]
            pricelist.append(price)
            totalprice += price
            itemlist.append(item)
            quantitylist.append(quantity)
        else:
            print("Sorry, the item you entered is unavailable.")
    else:
        print("You entered wrong number")

inp = input("Can I move to billing? Yes or No: ")
if inp.lower() == 'yes':
    if totalprice != 0:
        gst = (totalprice * 5) / 100
        finalamount = gst + totalprice
        print("\n-------BILLING-------")
        print("Customer Name:", name)
        print("Date:", datetime.now())
        print("---------------------")
        for i in range(len(itemlist)):
            print(f"{itemlist[i]} x {quantitylist[i]} = Rs {pricelist[i]}")
        print("---------------------")
        print("Total Price:", totalprice)
        print("GST (5%):", gst)
        print("Final Amount:", finalamount)
    else:
        print("No items purchased.")

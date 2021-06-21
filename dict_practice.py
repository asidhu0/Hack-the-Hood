grocery_list = {"chicken" : 1.59, "beef": 1.99, "cheese" : 1.00, "milk": 2.50}
nfl_players = {"tom brady" : 43, "george kittle" : 27, "patrick mahomes": 25, "aaron rodgers": 37}

chicken_price = grocery_list["chicken"]
beef_price = grocery_list["beef"]
cheese_price = grocery_list["cheese"]
milk_price = grocery_list["milk"]

brady_age = nfl_players["tom brady"]
kittle_age = nfl_players["george kittle"]
mahomes_age = nfl_players["patrick mahomes"]
rodgers_age = nfl_players["aaron rodgers"]

nfl_players ["tom brady"] += 1
nfl_players ["george kittle"] = 25
nfl_players ["patrick mahomes"] -= 2
nfl_players ["aaron rodgers"] += 3

shoe_inv = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
# print(shoe_inv)

shoe_inv ["SB Dunk"] -= 2
# print(shoe_inv)

shoe_inv ["Yeezy"] += 1
# print(shoe_inv)

shoe_inv["Jordan 13"] += 7
shoe_inv["Yeezy"] += 7
shoe_inv["Foamposite"] += 7
shoe_inv["Air Max"] += 7
shoe_inv["SB Dunk"] += 7
# print(shoe_inv)

shoe_inv["Jordan 13"] -= 3
shoe_inv["Yeezy"] -= 3
shoe_inv["Foamposite"] -= 3
shoe_inv["Air Max"] -= 3
shoe_inv["SB Dunk"] -= 3
# print(shoe_inv)

grocery_list ["cookies"] = 3.10
grocery_list["chips"] = 2.15
grocery_list ["yogurt"] = 4.45
# print(grocery_list)
nfl_players ["Nick Bosa"] = 23
nfl_players ["Dre Greenlaw"] = 24
nfl_players ["Fred Warner"] = 24
# print(nfl_players)
shoe_inv ["Air Jordan 1"] = 3
shoe_inv ["Ultraboosts"] = 15
shoe_inv ["Pegasus"] = 9
# print(shoe_inv)

del grocery_list ["cheese"]
del grocery_list ["beef"]
# print(grocery_list)
del nfl_players ["aaron rodgers"]
del nfl_players ["patrick mahomes"]
# print(nfl_players)
del shoe_inv ["Pegasus"]
del shoe_inv ["SB Dunk"]
# print (shoe_inv)

#add two items together to know the cost
def total_price (item1, item2):
    price = grocery_list[item1] + grocery_list[item2]
    return ("The total price of beef and cheese is" + int(price))

def price_difference (item1, item2):
    price = grocery_list[item1] - grocery_list[item2]
    return price ("The difference between beef and chees is" + abs(int(price)))

def restock (shoe_name, multiplier):
    newInventory = (shoe_inv[shoe_name] * multiplier)
    shoe_inv[shoe_name] = newInventory
    return newInventory 

def clearance_sale (shoe_name, discount):
    sale_price = (shoe_inv[shoe_name] / discount)
    shoe_inv[shoe_name] = sale_price
    return shoe_inv

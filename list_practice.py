city_names = [ "Oakland", "Atlanta", "New York City", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]

nba_players = [ "Russell Westbrook", "Stephen Curry", "Jayson Tatum", "Zion Williamson", "Ja Morant", "Luka Doncic", "Kevin Durant", "Kobe Bryant", "Nikola Jokic", "Lebron James"]

# print(city_names[6])
# print(city_names[2])
# print(city_names[0])

# print(nba_players[0])
# print(nba_players[1])
# print(nba_players[7])

three_cities = city_names[0:3]
# print(city_names[0:3])

four_cities = city_names[2:6]
# print(four_cities[2:6])

fav_players = nba_players[5:8]
# print(fav_players[5:8])

city_names [0] = "San Francisco"
city_names [2] = "Boston"
city_names [6] = "Hollywood"
city_names [4] = "Tampa"

nba_players [8] = "Klay Thompson"

city_names.append("New Jersey")
city_names.extend(["Santa Cruz", "Selma", "Chicago"])
city_names.insert(7, "Washington, D.C.")
# print(city_names)

del city_names [7]
city_names.pop(0)
city_names.remove("Boston")

# while loop to access all values 
# access value with index
# check to make sure that index is less than list length

def printCityNames ():
    counter = 0 
    while counter < len(city_names):
        print(city_names[counter])
        counter +=1
    return "completed"
# printCityNames()

def printCityNames (cities_list):
    counter = 0 
    while counter < len(cities_list):
        print(cities_list[counter])
        counter +=1
    return "completed"
# printCityNames(city_names)

# [longer names ... shorter names]
# get the length of listitem1, listitem2 
# check if len[listitem1] > len[listitem2]
#    move on
#else 
#    remove listitem 
#    put list item at end 
# return new list

def organize_cities(cities_list):
    counter = 0 
    for city in cities_list:
        print(city)
        if (len(cities_list[counter]) > len(cities_list[counter+1])):
            counter+=1 
        else: 
            cities_list.remove(city)
            cities_list.append(city)
            counter+=1
    return cities_list

organize_cities(city_names)

def organize_cities(cities_list):
    
    for index in range(len(cities_list)):
        print(index)
    return "developing"

print(organize_cities(city_names))


def organize_cities(cities_list):

    for index in range(len(cities_list) - 1):
        if cities_list[index] >= cities_list[index + 1]:
            continue
        else: 
            city = cities_list[index]
            cities_list.pop(index)
            cities_list.append(city)
        return cities_list
print(city_names)
print(organize_cities(city_names))

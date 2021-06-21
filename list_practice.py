city_names = [ "Oakland", "Atlanta", "New York City", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]

nba_players = [ "Russell Westbrook", "Stephen Curry", "Jayson Tatum", "Zion Williamson", "Ja Morant", "Luka Doncic", "Kevin Durant", "Kobe Bryant", "Nikola Jokic", "Lebron James"]

print(city_names[6])
print(city_names[2])
print(city_names[0])

print(nba_players[0])
print(nba_players[1])
print(nba_players[7])

three_cities = city_names[0:3]
print(city_names[0:3])

four_cities = city_names[2:6]
print(four_cities[2:6])

fav_players = nba_players[5:8]
print(fav_players[5:8])

city_names [0] = "San Francisco"
city_names [2] = "Boston"
city_names [6] = "Hollywood"
city_names [4] = "Tampa"

nba_players [8] = "Klay Thompson"

city_names.append("New Jersey")
city_names.extend(["Santa Cruz", "Selma", "Chicago"])
city_names.insert(7, "Washington, D.C.")
print(city_names)

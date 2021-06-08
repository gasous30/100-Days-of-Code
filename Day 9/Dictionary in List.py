travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, total_visits, cities_list):
    added_country = {"country": country_name, "visits": total_visits, "cities": cities_list}
    travel_log.append(added_country)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

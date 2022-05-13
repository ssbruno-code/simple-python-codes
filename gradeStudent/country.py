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

def addNewCountry(country, visits, cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities,
    }
    travel_log.append(new_country)


addNewCountry("Russia", 2, ["Moscow", "Saint Petersburg"])
addNewCountry("Brasil", 8, ["Criciuma", "Florianópolis", "Palhoça", "Foz do Iguaçu"])
print(travel_log)




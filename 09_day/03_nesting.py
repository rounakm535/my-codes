# Nesting of Dictionary

capitals = {
    "France" : "Paris" , 
    "Germany" : "Berlin"
}

# Nesting a list in a dictionary

travel_log = {
     "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},    
    "Germany" : { "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 15}, 
}

# Nesting a dictionary in a list

travel_log = [
    { 
        "Country" : "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },    
    {
         "Country" :  "Germany",
         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
         "total_visits" : 15
    }, 
]
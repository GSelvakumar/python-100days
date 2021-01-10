capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log1 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],"total_visits": 5}
}

#Nesting Dictionary in a list

travel_log2 = [
    {
        "country":"France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country":"Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],"total_visits": 5
    }
]

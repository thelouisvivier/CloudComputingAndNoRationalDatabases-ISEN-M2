# Get and return city name
def get_city():
    city = input("Enter city (Lille/Paris/Rennes/Lyon) : ")
    if city == "Lille":
        name = "fr-lille"
    elif city == "Paris":
        name = "fr-paris"
    elif city == "Rennes":
        name = "fr-rennes"
    elif city == "Lyon":
        name = "fr-lyon"
    else:
        print("Wrong city name! Exciting...")
        exit(1)

    return name

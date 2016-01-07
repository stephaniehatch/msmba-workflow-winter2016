def cereal_milk(gettingData): 
    while gettingData:
        choice = raw_input("Enter c for cereal or m for milk, (return for done): ")
        if choice == "c" or choice == "C":
            menu_variation = "../menu.csv"
            return menu_variation
        elif choice == "m" or choice == "M":
            menu_variation = "../menu1.csv"
            return menu_variation
        elif choice != "m" and choice != "M" and choice != "c" and choice != "C":
            choice = raw_input("IDIOT. c OR m ONLY: ")
         
def get_more():
    getMore = raw_input("Are you ready for more yummies in your tummies? (Enter y or n) ")
    if getMore == "y":
        gettingData = True
    else:
        gettingData = False
    return gettingData

            
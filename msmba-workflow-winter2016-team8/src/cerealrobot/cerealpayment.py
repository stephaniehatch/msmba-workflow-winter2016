# this is a demo of the api
from cerealterminator_api import *

# Part 1
start_meal("Cereal Terminator", "Welcome to Cereal Terminator")

myMenu = get_menu('../menu.csv',"Our Menu")
show_menu(myMenu)

myOrder = create_order("John", 5)
get_choice(myMenu, myOrder)
show_order(myOrder)

tickets = prepare_food(myOrder)
for ticket in tickets:
    plate = pickup_food(ticket)
    serve_food(plate)



# Payment Part 
myBill = new_bill()
myBill.addOrder(myOrder)
show_bill(myBill)
complain_if_bill_bad(myBill)

membership = cereal_member()
membership

if membership == 0:
    myPaymentType = get_payment_type()
    collect_payment(myPaymentType, myBill)
else :
    secret = raw_input("Enter secret password for 10% off coupon code for your next bowl: ")
    if secret == "python":
        print      
        print "10% off coupon code: CEREAL TERMIN 8 ORS! "
    else :
        print     
        print "Poser!"    

end_meal("Thank you for eating at Cereal Terminator. ", "Have a nice day!")

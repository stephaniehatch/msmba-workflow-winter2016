from cerealterminator_api2 import *
from cerealormilk import *
# Stephanie was here
# introduction to Cereal Robot
start_meal("Cereal Terminator, Home of the Cereal Robot", "Where you can have anything... as long as it's cereal.")

#ask if they want cereal or milk
gettingData = True
getCereal = False
getMilk = False
counter = 0
orderlist = []
while gettingData and counter < 2:
    gettingData = get_more()
    counter = counter + 1
    if gettingData:
        menu_variation = cereal_milk(gettingData)
        if menu_variation == "../menu.csv" and 'c' in orderlist:
            print "Sorry you've already ordered that... proceed"
            break
        elif menu_variation == "../menu1.csv" and 'm' in orderlist:
            print "Sorry you've already ordered that... proceed"
            break            
        elif menu_variation == "../menu.csv":
            orderlist = orderlist + ['c','C']
        elif menu_variation == "../menu1.csv":
            orderlist = orderlist + ['m','M']
        myMenu = get_menu(menu_variation,"Pick Your Poison")
        show_menu(myMenu)
        
        if menu_variation == "../menu.csv":
            getCereal = True
            myOrderc = create_order("Terminator")
            get_choice(myMenu, myOrderc)
            myOrder = myOrderc
        else:
            getMilk = True
            myOrderm = create_order("Terminator")
            get_choice(myMenu,myOrderm)
    if getCereal == True and getMilk == False:
        myOrder = myOrderc
    elif getCereal == False and getMilk == True:
        myOrder = myOrderm
    elif getCereal == True and getMilk == True:
        myOrder = merge_orders(myOrderc, myOrderm)
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
        print "#######"
        print "#######"    
        print "Poser!"  
        print "#######"  
        print "#######"

end_meal("Thank you for eating at Cereal Terminator. ", "Have a nice day!")

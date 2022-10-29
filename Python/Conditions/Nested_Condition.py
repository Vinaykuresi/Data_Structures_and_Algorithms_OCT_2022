
# passanger_ticket_status = "Confirmed"

passanger_ticket_status = "Not Confirmed"

if(passanger_ticket_status == "Confirmed") : 

    passanger_lauggage_weight  = int(input("Enter the Passanger lauggage weight : "))

    weight_limit_allowed = 30

    extra_lauggage_charge = 0

    if (passanger_lauggage_weight >= 0 and passanger_lauggage_weight <= weight_limit_allowed):
        extra_lauggage_charge = 0
    elif (passanger_lauggage_weight > 30 and passanger_lauggage_weight <= 40):
        extra_lauggage_charge = (passanger_lauggage_weight - weight_limit_allowed) * 300 
    else : 
        extra_lauggage_charge = (passanger_lauggage_weight - weight_limit_allowed) * 500

    if (extra_lauggage_charge > 0):
        print("Please make the payment of : ", extra_lauggage_charge, " rs to clear the check-in")
    else:
        print("Your Check-in Cleared")

else :

    print("Sorry, you ticket is Not Confirmed")
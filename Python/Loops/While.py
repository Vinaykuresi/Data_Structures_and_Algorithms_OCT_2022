
baggage_count = 100

remaining_bags = baggage_count

while(remaining_bags > 0):

    picked_up_bags = int(input("Number of bags picked up bu Passanger : "))

    if(picked_up_bags <= remaining_bags) : 

        remaining_bags = remaining_bags - picked_up_bags

        print("Number of bags remained : ", remaining_bags)

    else : 
        print("The Picked up bags should be less than or equal to remaining bags.")
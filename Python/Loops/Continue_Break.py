
'''
    A ~ Adult person
    C ~ Child
    FC ~ Flight Captian 
    FA ~ Flight Attendant 
    Sp ~ Suspicious Person
'''

for passanger in "A", "A", "FC", "C", "FA", "SP", "A", "A":

    if(passanger == "FC" or passanger == "FA"):
        print("No Check required")
        continue

    if(passanger == "SP"):
        print("Declare Emergency in the Airport")
        break 

    if(passanger == "C" or passanger == "A"):
        print("Proceed with Normal Security check.")

    print("Check the person")
    print("Check the person baggage.")
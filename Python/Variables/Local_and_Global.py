wt_limit = 20

print(wt_limit)

def baggage_weight_check(baggage_weight):
    extra_luaggage_charge = 0
    global wt_limit
    wt_limit = 30
    print(wt_limit)
    if(baggage_weight > wt_limit):
        extra_luaggage_weight = baggage_weight - wt_limit
        extra_luaggage_charge = extra_luaggage_weight * 100

    return extra_luaggage_charge



print(baggage_weight_check(40))

print(wt_limit)
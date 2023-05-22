# Flat 10
def flat_10(PT):
    Total = PT - 10
    return Total

# Bulk 5
def bulk_5(PT):
    Total = PT * 95/100
    return Total
# Bulk 10
def bulk_10(PT):
    Total = PT * 90/100
    return Total
# Tiered 50
def tiered_50(quantity_A,quantity_B,quantity_C):
    TA = 0
    TB = 0
    TC = 0
    if quantity_A> 15:
        TA = 15*20 + (quantity_A-15) * 20 * (50/100)
    else:
        TA = quantity_A * 20 
    if quantity_B> 15:
        TB = 15*40 + (quantity_B-15) * 40 * (50/100)
    else:
        TB = quantity_B * 40 
    if quantity_C> 15:
        TC = 15*50 + (quantity_C-15) * 50 * (50/100)
    else:
        TC= quantity_C * 50 
    TT = TA + TB + TC
    return TT
from func import *

quantity_A = int(input("Enter the number of 'Product A' required: "))
quantity_B = int(input("Enter the number of 'Product B' required: "))
quantity_C = int(input("Enter the number of 'Product C' required: "))
gift = input("Is this a Gift? (Y/N)")
Subtotal = quantity_A * 20 + quantity_B * 40 + quantity_C *50
total_quantity = quantity_A + quantity_B + quantity_C

# Number of Products added to cart
if quantity_A != 0:
    print("Total Price of Product A for",quantity_A,"items = ",quantity_A * 20)
if quantity_B != 0:
    print("Total Price of Product B for",quantity_B,"items = ",quantity_B * 40)
if quantity_C != 0:
    print("Total Price of Product C for",quantity_C,"items = ",quantity_C * 50)

# Subtotal
print ("Subtotal = ", Subtotal)

# Coupon Code
if Subtotal > 200:
    if (total_quantity>10) & (total_quantity<=20):
        print("The coupon code bulk_5 is applied")
        total = bulk_5(Subtotal)
    elif (total_quantity>20) & (total_quantity<=30):
        print("The coupon code bulk_10 is applied")
        total = bulk_10(Subtotal)
    elif (total_quantity>30) and (quantity_A > 15) or (quantity_B > 15) or (quantity_C > 15):
        print("The coupon code tiered_50 is applied")
        total = tiered_50(quantity_A,quantity_B,quantity_C)
    else:
        print("The coupon code flat_10 is applied")
        total = flat_10(Subtotal)
else:
    total = Subtotal
    print ("Total amount :",Subtotal)

# Discount Amount 
print("Discount amount :",Subtotal - total)

# Gift Wrap
if (gift == 'y') or (gift == 'Y'):
    gift_amount = total_quantity
else:
    gift_amount = 0

print("Gift wrap fee: ",gift_amount)

# Shipping Fee
if total_quantity > 0:
    shipping_units = total_quantity // 10
    if total_quantity % 10 !=0 :
        shipping_units += 1
    shipping_fee = shipping_units * 5

print ("Shipping fee :",shipping_fee)

# Total Amount
TotalAmount= total+gift_amount+shipping_fee
print ("Total amount :",TotalAmount)
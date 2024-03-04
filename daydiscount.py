from datetime import datetime
 
subtotal = " "
#processing
date = datetime.now()
#week_day = date.weekday()
week_day = 1
 
# while loop stretch challenge #2
while subtotal != 0:
    subtotal = float(input("Subtotal: "))
    # if tuesday or wensday continue
    if week_day == 1 or week_day == 2:
        if subtotal >= 50:
            discount = subtotal * 0.10
            print(f"Discount amount: {discount:.2f}")
            subtotal = subtotal - discount
        # stretch challenge #1 print the diffrence left to get discount.
        else:
            diff = 50 - subtotal
            print(f"Line 22 You only need to spend {diff:.2f} more dollars to get a 10% discount")
           
       
    tax = subtotal * 0.06
    subtotal = subtotal + tax
 
#output
 
    print(f"Sales tax amount: {tax:.2f}")
    print(f"total {subtotal:.2f}")





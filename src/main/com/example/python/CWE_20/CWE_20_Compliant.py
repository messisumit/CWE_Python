
# Improper input validation
def quantity():
    return -1  #negative value causes user account credit instead of debit

def charge(total):
    balance =200
    return balance-total

price =20
quantity  = quantity()
if quantity >=1:
    total = price*quantity
    print(charge(total))
else:
    print("invalid quantity")
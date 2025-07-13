#filter out quantity zero calculate total price for each valid order 
#calculate total bill using reduce

from functools import reduce
order=[
    {'items':'Laptop','price':50000,'quantity':1},
    {'items':'Mouse','price':500,'quantity':-1},
    {'items':'Keyboard','price':1500,'quantity':2},
    {'items':'Monitor','price':12000,'quantity':1},
    {'items':'Cabale','price':1000,'quantity':3}
]

qty=filter(lambda x:x['quantity']>0,order)
#print(list(qty))
bill=map(lambda x:x['price']*x['quantity'],qty)
#print(list(bill))
total=reduce(lambda x,y:x+y,bill)
print(total)


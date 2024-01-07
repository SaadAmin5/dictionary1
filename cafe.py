#task12

#menu list showing four items sold in the cafe
menu=['burger', 'pizza', 'chocolate', 'drink']

#stock dictionary containing the stock value for each item on menu
stock={'burger':50,  
       'pizza':40, 
       'chocolate':33, 
       'drink':40}

#price dictionary containing the prices for each item on menu
price= {'burger': 8, 
        'pizza': 9, 
        'chocolate':3, 
        'drink':2}

#calculating total stock worth in the cafe
sum=0
for item in menu:

    item_value=stock[item]* price[item]
    print(item,':', stock[item] ,'(stock)','*', price[item], '(price)','=', item_value)
    sum=sum+item_value

print()
print('Total stock worth in the cafe:',sum)
##
#Author: Dylan Garrett
#Date: 9/26/2016
#Description: This project programs a soda machine to perform its tasks
#
##


def power_on(name, price, quantity):
    '''Intial function that starts once the vending machine is powered on. '''
    global cans, price_per_can, product_name, balance
    balance = 0
    cans = 0
    
    if quantity > 0:
        cans = quantity
        
    elif quantity < 0:
        cans = 0
    
    if price < 0.0:
        price_per_can = 0.01
        
    else: 
        price_per_can = price
        
    
        
        
    
    if name == "":
        product_name = "undefined"
        
    else:
        product_name = name
    
    
    

def set_product_name(new_name):
    '''This function programs in a new name for the product inside the vending machine'''
    
    global product_name
    
    product_name = new_name
    
    if new_name == "":
        product_name = "undefined"
        
        
    else:
        product_name = new_name
        
    print("The new product name is: " + product_name)
        
    
def add_stock(number_added_cans):
    '''This function allows the user to add cans into the machine up to a certain number of cans'''
    global cans
    
    cans = number_added_cans + cans
    
    if number_added_cans < 0: 
        cans = cans
        print("The new stock of cans is: " + str(cans))
    
    if cans > 40:
        cans = "Error 405: To many cans"
        print(cans)
        
    
    else:
        print("The new stock of is cans: " + str(cans))
        
    
        
def set_price(new_price):
    '''this function lets the user set the price for the product'''
    global price_per_can
    
    price_per_can = new_price
    
    if price_per_can < 0:
        price_per_can = 0.01
        
    else: 
        price_per_can = new_price
    print("Comfirmed price change. Now set: $ " + str(price_per_can))
    

        
def insert_coins(currency):
    '''This function takes a customers currency and converts it to either sell a can with approiate change or return all money'''
    global price_per_can, balance, cans_sold, cans
    price_per_can = price_per_can
    
    cans_sold = 0
    
    verify_cans = cans
    
    change = currency - price_per_can
    
    balance = price_per_can * cans_sold
    
    if cans_sold > 0:
        cans = cans - cans_sold
    
    if currency < price_per_can:
           
        return("Insufficient funds change returned: $" + str(currency))
            
    elif currency >= price_per_can:
        cans_sold = cans_sold + 1
        change = currency - price_per_can
        return("Drink Sold " + "\n"
        + "Change Returned $ " + str(change))
        
    #else: 
        #currency = change
        #return("Charge returned: $" + str(currency))
            
        
            
    if cans <= 0:
        verify_cans = "Insuffcient Stock"
        return(verify_cans)
        
    else: verify_cans = cans
    
        
            
        
    return("cans sold" + str(cans_sold))
    
    
            
    

def empty_coins():
    '''When the owner empties the currency out of the machine'''
    global balance, price_per_can, currency, cans_sold
    cans_sold = cans_sold
    
    balance = price_per_can * cans_sold
    
    temp_balance = balance
    
    empty_balance = temp_balance - balance
    
    print("Total Currency: $ " + str(temp_balance))
    print("Balance Zeroed: " + str(empty_balance))


def report():
    '''Prints a report that shows the owner the current price per can, how many cans are in stock, the current name of the product, and the balance in the machine'''
    global price_per_can, cans, product_name, balance
  
  
    print("Report:" + "\n" 
    + "==========" + "\n" +
    "Product Name " + product_name + "\n" +
    "Stock " + str(cans) + "\n" +
    "Price $" + str(price_per_can) + "\n" +
    "Balance $ " + str(balance))
 
    
'''  
power_on("Irn Bru",1.20, 5)
set_product_name("Cat")
add_stock(3)
set_price(2.50)
insert_coins(2.50)
empty_coins()
report()
'''
    
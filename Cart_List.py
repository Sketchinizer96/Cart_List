# this is an example for list that will involve a online shopping cart as an example from typing import List
from typing import List, Dict, Any

print("*" * 10 + " Welcome to Online Shopping Cart " + "*" * 10)
print("Please Enter a User Name and Password")
# Here we check the truely and falsely conditions
username = (input(f"Please enter the User_Name : \t"))
password = (input(f"Please enter the Password : \t"))
a: bool = False  # declaring a Global variable
if bool(username) is False and bool(password) is False:  # Converting the value to Boolean as they are in string format
    print(' Please enter the user name and password :: Invalid input')
if password.isalnum():  # Checks the is alphanumeric
    print('Password Excepted')
    a: bool = True
else:
    print('Password Not alpha Numeric')
value_b: int = a  # type casting boolean to integer

if value_b == 1:
    encrypted_password = password.encode(encoding="ascii", errors="ignore")
    # print(encrypted_password)
    password_length = len(encrypted_password)  # calculate length of the password
    encrypted_password_1 = '*' * password_length  # print the number of stars as per length
    print(f'##Username : {username} \n##Password : {encrypted_password_1}')
print(f'\t'+ '-' * 99 )
print('****** Welcome to Shopping Cart ******')
print('Please Begin Shopping')
username_a: list = username.split(" ", 1)
print('User : ' + username_a[0])
# inventory code Begins here
inventory = [{
    'Mobile': [{'oppo': [{'X1': 20, 'X2': 50, 'X3': 60}],
                'vivo': [{'Z1': 20, 'Z2': 50, 'Z3': 60}],
                'xiaomi': [{'M1': 20, 'M2': 50, 'M3': 60}]}],
    'Food': [{'grapes': [{'BEST': 60, 'GOOD': 50, 'AVERAGE': 20}],
              'apple': [{'BEST': 60, 'GOOD': 50, 'AVERAGE': 20}],
              'banana': [{'BEST': 60, 'GOOD': 50, 'AVERAGE': 20}]}],
    'Headphones': [{'apple': [{'A1': 20, 'A2': 50, 'A3': 60}],
                    'jbl': [{'B1': 20, 'B2': 50, 'B3': 60}],
                    'sony': [{'C1': 20, 'C2': 50, 'C3': 60}]}]
}]
print(f'Inventory consists of :\n \t1:Mobile\n\t2:Food\n\t3:Headphones')
print('*' * 100)
selection = input('Please enter the Selection name : ')
selection_1 = list((inventory[0][selection][0]).keys())   # returns all the value of the dictionary as kes
print(f'Following are the available options for {selection} :' + str(selection_1))
print('*' * 100)
item = input('Please enter the value to see the contents of the Items :')
sub_item = list((inventory[0][selection][0][item]))     # selects sub items and typecast to list and store it
# item_index = item_keys.index(item)
# print(item_index)
# sub_item = (inventory[0][selection][0])
print(f'List of Sub_Items for {item} Brand and its Price : ' + str(sub_item[:]))
print('*' * 100)
brand: str = input(f'Please enter the selection brand for {item} and check out the price :  ')
price = (inventory[0][selection][0][item][0][brand])  # grabs the price for the brand
print('*' * 100)
print("Please Start the purchase of items")
selection_item = list((inventory[0][selection][0][item]))
print(str(selection) + ' : ' + str(item) + ' : ' + str(brand) + ' : ' + str(price))
print('*' * 100)
print('Do you want to add the item to the Bag')
response = input(f'Yes / No :\t')
bag_list = []
if response == 'Yes':
    bag_list.append(item)
    print('item added to bag')
elif response == 'No':
    print(f'You added  {item} of {brand} priced at {price} to the Bag')
print('*' * 100)
print('Do you want to Purchase and View the Invoice :')
response_2 = input(f'Yes / No :\t')
if response_2 == 'Yes':
    print(f'\t'+ '-' * 99 )
    print(f'\t'+('-' * 34) + 'INVOICE FOR PURCHASE '+('-' * 44))
    print(f'\t\t\t\tItem :{item} \t\t|\t\t Brand :{brand} \t\t|\t\t price :{price}')
    print(f'\t' + '-' * 99)
    print(f'\t'+('-' * 34) + f'THANK YOU {username} '+('-' * 36))

else:
    print('No items Purchased, Cart Empty')



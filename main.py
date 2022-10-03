#importing modules
import  json
import operations
from register import registration


#declaring variables
thanks ='Thanks for Banking With Us'
pincode_try = 2
pincode_try_count =0

#readig the file frm details file
filename = 'details.json'
with open(filename, 'r') as read_file:
    content = json.load(read_file)

print(content)


#program code
try:

    print('\nWelcome to NITACAGRA BAMKING SERVICES')
    name = input('\nWhats Your name: ').lower()

    if name == content['name']:
        print(name.title() ,' Enter Your pincode')
        pincode =  int(input(': '))
       
        while pincode_try_count < pincode_try: 
           
            
            if pincode == content['pincode'] :#pincode in content :
                 print(str(content['name']).title() ,str(content['surname']).title(),'How can we help you today')
                 print(operations.operations())
            else:
                print(name.title() ,' Renter Your pincode')
                pincode =  int(input(': '))
                pincode_try_count+=1
                
        else:
            print('Pinblocked\n',thanks)  
       
    else:
        print('\nHie',name.title() , 'Welcome Thanks for choosing us\nRegester your details,')
        print(registration())
except(ValueError):
    print('enter only digits')
#importing modules
import  json
import operations
from register import registration


#declaring variables
thanks ='Thanks for Banking With Us'
pincode_try = 2
pincode_try_count =0
outloop = False

#readig the file frm details file
filename = 'details.json'
with open(filename, 'r') as read_file:
    content = json.load(read_file)
#program code
try:

    print('\nWelcome to NITACAGRA BAMKING SERVICES')
    name = input('\nWhats Your name: ').lower()

    if name == content['name']:
        print(name.title() ,' Enter Your pincode')
        pincode =  int(input(': '))
        if pincode == content['pincode']:
            #outloop = False
            pass
        else:
            while  pincode != content['pincode'] and not(outloop)  : 
                if pincode_try_count < pincode_try:
                    attempts = pincode_try -pincode_try_count
                    print('You have' ,attempts,'Attempts Left')
                    pincode =  int(input('Renter Your pincode: '))
                    pincode_try_count+=1
                else:
                    outloop = True
                    break
                
        if outloop:
            print('Pinblocked\n') 
            
        else:
            print(str(content['name']).title() ,str(content['surname']).title(),'How can we help you today')
            operations.operations()
            print('\n')
            
    else:
        print('\nHie',name.title() , 'Welcome Thanks for choosing us\nRegester your details,')
        registration()
except(RuntimeError()):
    print('enter only digits')
except(ValueError()):
    print('enter only digits')
    
except(FileNotFoundError()):
    print('enter only digits')
    
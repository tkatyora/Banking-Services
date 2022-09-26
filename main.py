#The simple version
import  json
import operations
filename = 'details.json'
with open(filename, 'r') as read_file:
    content = json.load(read_file)
thanks ='Thanks for Banking With Us'
#peogram code
try:

    print('\nWelcome to NITACAGRA BAMKING SERVICES')
    name = input('\nWhats Your name: ').lower()

    if name == content['name']:
        print(name.title() ,' Enter Your pincode')
        pincode =  int(input(': '))
        if pincode == content['pincode'] : #pincode in content
            print(str(content['name']).title() ,str(content['surname']).title(),'How can we help you today')
            print(operations.operations())
        else:
            print('Wrong pincode\n',thanks)
    else:
        print(name.title(),' Please Go and register first')
except(ValueError):
    print('enter only digits')
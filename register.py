import  json
thanks = 'Thanks for Banking With Us'
filename = 'details.json'
file_surname = 'surname.json'
file_pin_code = 'pin.json'
class person:
    def __init__(self, name:str, surname:str, pincode:int,balance=0):
        self.Name = name
        self.Surname = surname
        self.Pincode = pincode
        self.Balance = balance
try:

    print('Hie welcome to NITACAGRA BAMKING SERVICES\nRegester your details')
    name = input('\nEnter Your name: ').lower()
    surname = input('Enter Your surname: ').lower()
    pincode = int(input('Enter Your pincode: '))
    person =person(name,surname,pincode,)
    details={'name': person.Name ,'surname':person.Surname,'pincode':person.Surname,'balance':person.Balance}
    # details = [name, surname, pincode]
    print('Your entered details\n' ,name.title() ,'\n' ,surname.title() , '\n', pincode)
    choice = input('\nPress  1.Confirm   2.Cancel\n: ')


    if choice == '1':

        with open(filename , 'w') as write_file :
           json.dump(details, write_file)
        print('\n',name.title(),' ' , surname.title(),' ' ,thanks)
    elif choice == '2':
        print('\n', name.title(), ' ', surname.title(), ' ', thanks)
        pass
    else:
        print('Entered Invalid Option')


except(ValueError):
    print('\nPlease Enter only numbers')
    pass
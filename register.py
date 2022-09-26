import  json
import  sys
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

    def calculate_withdrwal(balance):
        withdrawal = 0.7 * balance
        return  withdrawal
try:
    # exit = input('Press Q to exit').lower()
    print('Hie welcome to NITACAGRA BAMKING SERVICES\nRegester your details,'
          'Press Q if you wish to exit the resistation')
    name = input('\nEnter Your name: ').lower()
    surname = input('Enter Your surname: ').lower()
    while True:
        pincode = int(input('Enter Your pincode: '))
        confirm_pincode = int(input('ReEnter Your pincode: '))

        if exit == 'q':
            sys.exit()
        if pincode == confirm_pincode:
            break
        else:
         print('\nPincode doest match Reenter pincode\n')
    person =person(name,surname,pincode,)
    details={'name': person.Name ,'surname':person.Surname,'pincode':person.Pincode,'balance':person.Balance}
    # details = [name, surname, pincode]
    print('\nYour entered details\n' ,name.title() ,'\n' ,surname.title() , '\n', pincode)
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
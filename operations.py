import sys
from getpass import getpass
def operations():
    import json
    # reading the details  pf the user
    details = 'details.json'
    with open(details, 'r') as read_file:
        content = json.load(read_file)
    # Calculating the amount thata should allow withdrwal
    try:
        
        amount_withdrwal = 0.7 *content['balance']
            
    

        # dtarting the operations
        choose = input('''
    1.Balance
    2.Withdrawal
    3.Deposit
    4.Change Pin
    5.Profile
    : ''')
        if choose == '1':
                print('Your balance is $',content['balance'])
        elif choose == '2':
            withdrawal = int(input('Enter ammonut to withdraw:\n$'))
            if withdrawal <= amount_withdrwal:
                new_balance = content['balance'] - withdrawal
                with open(details,'w') as write_file:
                    new_details = {'name':content['name'],'surname':content['surname'],'pincode':content['pincode'],'balance':new_balance}
                    json.dump(new_details,write_file)
                print('Withdrwawll successfull!')
            else:
                print('Insufficient funds!')

        elif choose == '3':
            deposit = int(input('Enter amount to deposit :\n$'))
            #adding the deopisted to the existing balabce
            new_balance = content['balance'] + deposit
            # ading the amount deposited to the balance file
            with open(details, 'w') as write_file:
                new_details = {'name':content['name'],'surname':content['surname'],'pincode':content['pincode'],'balance':new_balance}
                json.dump(new_details,write_file)
            print('Deposited succefully!')
        elif choose == '4':
            print('Your old pin was:',content['pincode'])
            new_pin= int(getpass('Enter New Pin: '))
            confirm_pin = int(getpass('Reenter pin: '))
            new_details = {'name':content['name'],'surname':content['surname'],'pincode':new_pin,'balance':content['balance']}
            if new_pin == confirm_pin:
                with open(details, 'w') as write_file:
                    json.dump(new_details,write_file)
                print('Pin Changed Succesfully')
            else:
                print('pin doest match')

        elif choose == '5':
            print('\nYour Profile')

            for title,data in content.items():
                print(str(title).title(),':',str(data).title())


        else:
            print('Invalid Option')
            return operations
    except():
        print('Wrong key selected')
        sys.exit()

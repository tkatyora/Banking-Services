
def operations():
    import json
    # reading the lbance that is in the balance.json file
    balancefile = 'balance.json'
    with open(balancefile, 'r') as read_file:
        balance = int(json.load(read_file))
    # reading the details  pf the user
    filename = 'details.json'
    with open(filename, 'r') as read_file:
        content = json.load(read_file)
    # Calculating the amount thata should allow withdrwal
    amount_withdrwal = 0.7 * balance

    # dtarting the operations
    choose = input('''
1.Balance
2.Withdrawal
3.Deposit
4.Change Pin
5.Profile
: ''')
    if choose == '1':

            print('Your balance is $',balance)
    elif choose == '2':
        withdrawal = int(input('Enter ammonut to withdraw:\n$'))
        if withdrawal <= amount_withdrwal:
            new_balance = balance - withdrawal
            with open(balancefile ,'w') as write_file:
                json.dump(new_balance,write_file)
            print('Withdrwawll successfull!')
        else:
            print('Insufficient funds!')

    elif choose == '3':
        deposit = int(input('Enter amount to deposit :\n$'))
        #adding the deopisted to the existing balabce
        new_balance = balance + deposit
        # ading the amount deposited to the balance file
        with open(balancefile, 'w') as write_file:
            json.dump(new_balance,write_file)
        print('Deposited succefully!')
    elif choose == '4':
        print('Your old pin was:',content['pincode'])
        new_pin= int(input('Enter New Pin: '))
        confirm_pin = int(input('Reenter pin: '))
        details = [content['name'],content['surname'],new_pin]
        if new_pin == confirm_pin:
            with open(filename, 'w') as write_file:
                json.dump(details, write_file)
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


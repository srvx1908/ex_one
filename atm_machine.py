b=16368
PIN=1234
chances = 3
print('*WELCOME TO SBI')
while chances>=0:
    x=int(input('Enter PIN Number: '))
    if x==PIN:
        print('*Login Sucessful*')
        x = int(input('Press 1 to continue: '))
        if x == 1:
            print('1. Check Balance')
            print('2. Withdraw Amount')
            d=int(input('Enter Your Choice: '))
            if d==1:
                print('Your Balance is:')
                print(b)
            elif d==2:
                w=int(input('Enter amount to withdraw:'))
                if w<b:
                    print('withdraw successful')
                    b=b-w
                else:
                    print('insufficient funds')
        else:
            print('Successfully Logged Out')
    else:
        print('Invalid Password')
        chances=chances-1
        if chances==0:
            print('*Account Blocked*')
            break
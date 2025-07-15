

balance = 100


choice = None

while (choice != 5):
    choice = int(input('Please choose one of the following options \n1. adding funds\n2. checking balance\n3. reporting lost card \n4. access to resources \n5. quit\n'))

    if choice==1:
        choice_input = input('Add cash or Debit card \na. cash\nb. debit\n')
#a.20 dollars \nb.40 dollars \nc.50 dollars \nd.100 dollars \nchoose your amount a/b/c/d \n'
        choice_input = input('Please enter the amount of money you would like to add to the CatCard\n')
        while (int(choice_input) < 0) :
            print('Invalid Input')
            choice_input = input('Please enter the amount of money you would like to add to the CatCard\n')
        balance += int(choice_input)
        print(balance)
        #balance = balance + choice_input

        #Figure out a way to, based on the user's inputs, increase the amount in the cat card
    if choice ==2:
        print('Check avaiable balance: \n')
        #Figure out a way to print out the available balance in the card
        print(balance)
    if choice ==3:
        choice_input= input('report lost or stolen \na.lost \nb.stolen\n')
        choice_input= input('report completed\n')
        #Figure out a way to do ...
    if choice ==4:
        choice_input= input('more options \na.report \nb.canvas \nc.library\n')
        choice_input=('choice completed\n')
        #What do we do here?
        

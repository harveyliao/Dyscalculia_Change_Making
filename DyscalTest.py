from change_making import *

x = dyscal()
print("Please setup your wallet")
x.AskResetWallet()

'''
x.ResetWallet(10,10,10,1,1,\
              1,1,2,0,0)
amount = 156.7
comb = x.ChangeMaking(amount)[2]
print("Total money paid at first:", x.SumList(comb))
'''


while True:
    amount = eval(input("Enter the number on the cashier:"))
    change_comb = x.ChangeMaking(amount)
    '''
    ref self.ChangeMaking()
    1st element is T/F means enough(True) in wallet or not(False)
    2nd element is T/F means need change(True) ot not(False)
    3rd element is the payment combination that the algorithm give
    If need to ask for change, the amount you should receive from the cashier is the 4th elemeny
    '''
    print("Total money paid at first:", "{0:.2f}".format(x.SumList(change_comb[2])))
    if (change_comb[0] == True) and (change_comb[1] == False):
        #Enough money and No change required
        x.SubtractListFromWallet(change_comb[2])
    if (change_comb[0] == True) and (change_comb[1] == True):
        #Enough money and Do require change
        x.SubtractListFromWallet(change_comb[2])
        print("Please enter the changed money, it should be:$", change_comb[3])
        New_change = x.AskForInput()
        if New_change == change_comb[3]:
            x.AddListToWallet(New_change)
        else:
            print("you are not getting right change!")
            diff = New_change - change_comb
            if (diff > 0):
                print("#CHECKPOINT#Return $", diff, "to the cashier")
            if (diff < 0):
                print("#CHECKPOINT#Ask cashier for $", diff)
            #CHECKPOINT#
            #need to verify the newer new_change
    x.ShowWallet()

'''
Testing log:

Case #1
x.ResetWallet(10,10,10,1,1,\
              1,1,2,0,0)
$156.7 : ask for $1.8000000000000114 change
                        ^ that is wierd, ref to line 222
        solved by formating it as print("{0:.2f}".format(a)), where .2f means 2 decimal point
        ref: https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

'''

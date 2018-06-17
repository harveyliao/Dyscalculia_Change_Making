from change_making import *

x = dyscal()
#print("Please setup your wallet")
#x.AskResetWallet()
print("Set the wallet as 1 for each dominant.")
test_list = [1] * 10
x.ResetListWallet(test_list)
x.ShowWallet()

'''
x.ResetWallet(10,10,10,1,1,\
              1,1,2,0,0)
amount = 156.7
comb = x.ChangeMaking(amount)[2]
print("Total money paid at first:", x.SumList(comb))
'''


while True:
    amount = eval(input("Enter the price on the cashier:"))
    change_comb = x.ChangeMaking(amount)
    '''
    ref self.ChangeMaking()
    1st element is T/F means enough(True) in wallet or not(False)
    2nd element is T/F means need change(True) ot not(False)
    3rd element is the payment combination that the algorithm give
    If need to ask for change, the amount you should receive from the cashier is the 4th elemeny
    5th element is the return code, planned to be used in the next version
             code: meaning
                0: not enough
                1: pay all bills and coins
                2: pay all bills
                3: pay all coins
                4: exact combination as return[2]
                5: ask for change as return[3], further confirmation needed
    '''
    print("Total money paid:", "{0:.2f}".format(x.SumList(change_comb[2])))
    if (change_comb[0] == True) and (change_comb[1] == False):
        #Enough money and No change required
        print("Payment finished! No change required")
        x.SubtractListFromWallet(change_comb[2])
    if (change_comb[0] == True) and (change_comb[1] == True):
        #Enough money and Do require change
        x.SubtractListFromWallet(change_comb[2])
        print("Please follow the instructions to enter the change, it should be: $" + change_comb[3])
        New_change = x.AskForInput()
        if x.SumList(New_change) == (float)(change_comb[3]):
            print("Payment finished! You get the right change back.")
            x.AddListToWallet(New_change)
        else:
            print("you are not getting right change")
            #print("New_change:", New_change, "change_comb[3]:", change_comb[3])  #debuging
            diff = x.SumList(New_change) - (float)(change_comb[3])
            if (diff > 0):
                print("*NEXT STEP* Return $", "{0:.2f}".format(diff), "to the cashier")
            if (diff < 0):
                print("*NEXT STEP* Ask cashier for $", "{0:.2f}".format(diff))
            #NEXT STEP: need to verify the newer new_change is right
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

class dyscal:
    def __init__(self):
        '''
        self.wallet maintain the current virtual wallet in app
        self.value is the denomination
        self.Ccurrency_List id thier name
        '''
        self.wallet = [0, 0, 0, 0, 0,\
                       0, 0, 0, 0, 0]
        self.value = [100, 50, 20, 10, 5, \
                      2, 1, 0.25, 0.1, 0.05]
        self.Currency_List = ["$100", "$50", "$20", "$10", "$5", \
                         "$2", "$1", "¢25", "¢10", "¢5"]

    def ResetWallet(self, hundred, fifty, twenty, ten, five, \
                    two, one, quater, tencent, fivecent):
        '''
        Reset the self.wallet in way of command line
        :param hundred: The amount of 100 dollar
        :param fifty: The amount of 50 dollar
        :param twenty: The amount of 20 dollar
        :param ten: The amount of 10 dollar
        :param five: The amount of 5 dollar
        :param two: The amount of 2 dollar
        :param one: The amount of 1 dollar
        :param quater: The amount of 25 cents
        :param tencent: The amount of 10 cent
        :param fivecent: The amount of 5 cent
        :return:True
        '''
        self.wallet = [hundred, fifty, twenty, ten, five, \
                       two, one, quater, tencent, fivecent]
        return True

    def AddToWallet(self, hundred, fifty, twenty, ten, five, \
                    two, one, quater, tencent, fivecent):
        '''
        Add to the self.wallet in way of command line
        :param hundred: The amount of 100 dollar
        :param fifty: The amount of 50 dollar
        :param twenty: The amount of 20 dollar
        :param ten: The amount of 10 dollar
        :param five: The amount of 5 dollar
        :param two: The amount of 2 dollar
        :param one: The amount of 1 dollar
        :param quater: The amount of 25 cents
        :param tencent: The amount of 10 cent
        :param fivecent: The amount of 5 cent
        :return:True
        '''
        self.wallet += [hundred, fifty, twenty, ten, five, \
                       two, one, quater, tencent, fivecent]
        return True

    def SubtractFromWallet(self, hundred, fifty, twenty, ten, five, \
                    two, one, quater, tencent, fivecent):
        '''
        Subtract from the self.wallet in way of command line
        :param hundred: The amount of 100 dollar
        :param fifty: The amount of 50 dollar
        :param twenty: The amount of 20 dollar
        :param ten: The amount of 10 dollar
        :param five: The amount of 5 dollar
        :param two: The amount of 2 dollar
        :param one: The amount of 1 dollar
        :param quater: The amount of 25 cents
        :param tencent: The amount of 10 cent
        :param fivecent: The amount of 5 cent
        :return:True
        '''
        self.wallet -= [hundred, fifty, twenty, ten, five, \
                    two, one, quater, tencent, fivecent]
        return True

    def ResetListWallet(self, wallet_List):
        '''
        Reset the self.wallet to param. waller_List
        :param wallet_List: list w/ len()=10 in order of self.value
        :return: True
        '''
        self.wallet = wallet_List
        return True

    def AddListToWallet(self, wallet_List):
        '''
        Add the param. waller_List to self.wallet
        :param wallet_List: list w/ len()=10 in order of self.value
        :return: True
        '''
        #self.wallet += wallet_List  #not valid unless use numpy
        local_wallet = list(self.wallet)
        self.wallet = [(i + j) for i, j in zip(local_wallet, wallet_List)]
        return True

    def SubtractListFromWallet(self, wallet_List):
        '''
        Subtract the param. waller_List from self.wallet
        :param wallet_List: list w/ len()=10 in order of self.value
        :return: True
        '''
        #self.wallet -= wallet_List  #not valid unless use numpy
        local_wallet = list(self.wallet)
        self.wallet = [(i - j) for i, j in zip(local_wallet, wallet_List)]
        return True

    def ShowWallet(self):
        '''
        Show self.wallet
        :return: print a list, return True
        '''
        #print self.wallet in a convenient view
        print("Wallet status:")
        for i in range(0, 10):
            #print("The amount of " + self.Currency_List[i] + " is: ", self.wallet[i])
            print(self.Currency_List[i]," : ", self.wallet[i])
        return True

    def AskForInput(self):
        '''
        Present a dialog to get input from user, one denomination by one
        Currently used by AskResetWallet(), AskAddToWallet, AskSubtractFromWallet()
        :return: the input list w/ len() = 10, all elements are integer
        '''
        Input_List = [0]*10
        for i in range(0, 10):
            print("Enter the amount of " + self.Currency_List[i] + ":")
            Input_List[i] = input()
            #CAUTION: should add a while loop to verify the input is non-negative integer

        Input_List = [int(x) for x in Input_List]
        return Input_List
        '''
        #input confirmation loop, not working currently
        while True:
            Ask4Confirm = input("Is the input True?(yes/no)")
            if Ask4Confirm == "yes" or "y" or "Yes":
                Input_List = [ int(x) for x in Input_List]
                return Input_List
            elif Ask4Confirm == "no" or "n" or "No":
                self.AskForInput()
            else:
                print("Err: Input muust be 'yes' or 'no'")
        '''

    def AskResetWallet(self):
        '''
        Reset the self.wallet in way of dialogue
        :return: True
        '''
        Temp_wallet = self.AskForInput()
        self.wallet = Temp_wallet
        return True

    def AskAddToWallet(self):
        '''
        Add to the self.wallet in way of dialogue
        :return: True
        '''
        Temp_wallet = self.AskForInput()
        self.wallet += Temp_wallet
        return True

    def AskSubtractFromWallet(self):
        '''
        Subtract from the self.wallet in way of dialogue
        :return: True
        '''
        Temp_wallet = self.AskForInput()
        self.wallet = Temp_wallet

    def SumWallet(self, first = 0, last = 10):
        '''
        Sum self.wallet, by default, according to self.value
        could change param to sum from, say, 5th term to 10th term, by setting first=5 and last=10
        :param first: The starting point of summation, 0th by default
        :param last: The end point of summation, 10th by default
        :return: The summation
        '''
        return sum([self.wallet[i] * self.value[i] for i in range(first, last)])

    def SumList(self, wallet_list, first = 0, last = 10):
        '''
        Similar to SumWallet(). INstead of summing self.wallet, it sum param. wallet_list according to self.value
        :param wallet_list: list w/ len()=10
        :param first: The starting point of summation, 0th by default
        :param last: The end point of summation, 10th by default
        :return: False if len(wallet_list)!=10, otherwise return the summation
        '''
        if len(wallet_list) != 10:
            return False
        return sum([wallet_list[i] * self.value[i] for i in range(first, last)])

    def ChangeMaking(self, bill):
        '''
        The function to find combination of bills and coins according to the param. bill
        :param bill: the amount needed to pay
        :return: [True/False, True/False, [list w/ len() = 10 representing payment combination], AskForThisChange]
            1st element is T/F means enough(True) in wallet or not(False)
            2nd element is T/F means need change(True) ot not(False)
            3rd element is the payment combination that the algorithm give
            If need to ask for change, the amount you should receive from the cashier is the 4th elemeny
        '''
        origin_bill = bill
        #first find errors or lucky cases
        if bill > self.SumWallet():
            print("Sorry, you don't have enough money in your wallet")  #could be regulate as return code 0
            return [False, False, [0]*10, 0]
        if bill == self.SumWallet():
            print("Pay all bills and coins in the wallet")  #could be regulate as return code 1
            return [True, False, list(self.wallet), 0]
        if bill == self.SumWallet(0, 5):
            print("Pay all bills in the wallet")  #could be regulate as return code 2
            return [True, False, list(self.wallet)[0:5] + ([0]* 5), 0]
        if bill == self.SumWallet(5, 10):
            print("Pay all coins in the wallet")    #could be regulate as return code 3
            return [True, False, ([0]* 5) + list(self.wallet)[5:10], 0]
        #can pay the bill, need to find the combination of bills and coins
        if bill < self.SumWallet():
            #first assume there is a potential 'perfect combination' (exact combination that meets the bill)
            Change_combination = [0] * 10
            for i in range(0, 10):
                #print("currently at:", i) #test line
                MouduloCurrentDenomination = bill % self.value[i]
                #print("Modulo... currently at:", MouduloCurrentDenomination) #test line
                AmountOfCurrentDenomination = (bill - MouduloCurrentDenomination) / self.value[i]
                #print("AmountOfCurrentDeno... currently at:", AmountOfCurrentDenomination) #test line
                #print("list(self.wallet)", self.wallet[i])
                if AmountOfCurrentDenomination > list(self.wallet)[i]:
                    AmountOfCurrentDenomination = list(self.wallet)[i]
                Change_combination[i] = AmountOfCurrentDenomination
                bill -= AmountOfCurrentDenomination * self.value[i]
            if (bill == 0):
                #there is a 'perfect combination', int() it and return
                Change_combination = [int(x) for x in Change_combination]
                print("Pay the combination", Change_combination,"The amount is exact")  #could be regulate as return code 4
                return [True, False, Change_combination, 0]
            if bill > 0:
                #Add the smallest extra to make sure we can pay the bill
                local_wallet = list(self.wallet)  #since the next line doesn't accept function call to 'list()'
                dummy_wallet = [(i - j) for i, j in zip(local_wallet, Change_combination)]
                #[(i - j) for i, j in zip(a,b)]
                #vector subtract, actually dummy_wallet = list(self.wallet - Change_combination, but it's for syntax
                while True:
                    for i in range(9, -1, -1):
                        #search for the smallest available denomination
                        if (dummy_wallet[i] != 0) and (bill > 0):
                            #if it is able to spend one more that denonimation,
                            # then subtract it from dummy_wallet and see if it's enough
                            Change_combination[i] += 1
                            dummy_wallet[i] -= 1
                            bill -= list(self.value)[i]
                    if (bill <= 0):
                        break
                Change_combination = [int(x) for x in Change_combination]
                AmountOfChange = self.SumList(Change_combination) - origin_bill
                #float("{0:.2f}".format(AmountOfChange))  #doesn't work here, put this in print() function
                #print("self.SumList(Change_combination) is:", self.SumList(Change_combination))
                #print("origin_bill is:", origin_bill)
                #print("AmountOfChange is:", AmountOfChange)
                print("Pay the combination", Change_combination, "and ask for $", "{0:.2f}".format(AmountOfChange), "change")  #could be regulate as return code 5
                #CAUTION: return code 5 need furthur action on ensuring get right amount of change back
                return [True, True, Change_combination, "{0:.2f}".format(AmountOfChange)]
                '''
                #maybe doesn't work for some corner cases
                for i in range(9, -1, -1):
                    if (self.value[i] > bill) and dummy_wallet[i]:
                        print("Ask", self.value[i] - bill, "for change")
                        Change_combination[i] += 1
                        break
                return [ int(x) for x in Change_combination]
                '''

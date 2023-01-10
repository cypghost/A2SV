class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        
    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if  1 <= account1 <= len(self.balance) and 1 <= account2 <= len(self.balance):
            
            # checking if both accounts exist. and if the transaction would be valid
            if self.balance[account1 - 1] >= money:

                # performing the transaction
                self.balance[account1 - 1] -= money                
                self.balance[account2 - 1] += money

                return True
            
        return False

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        # if account exists performing transaction
        if 1 <= account <= len(self.balance):
            self.balance[account - 1] += money
            
            return True
        
        return False
        
    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        # checking if transaction is valid
        if 1 <= account <= len(self.balance) and self.balance[account - 1] >= money:
            
        # performing the withdraw
            self.balance[account - 1] -= money
        
            return True
            
        return False
        
        
#     def __init__(self, balance):
#         """
#         :type balance: List[int]
#         """
#         self.balance = balance
        
#     def transfer(self, account1, account2, money):
#         """
#         :type account1: int
#         :type account2: int
#         :type money: int
#         :rtype: bool
#         """
#         if 1 <= account1, account2 < bal and self.balance[account] >= money:
#               if self.withdraw(account1, money):
#                   if self.deposit(account2, money):
#                       return True
            
#         return False

#     def deposit(self, account, money):
#         """
#         :type account: int
#         :type money: int
#         :rtype: bool
#         """
#         bal = len(self.balance)
#         if 1 <= account < bal and self.balance[account] >= money::
#             self.balance[account] += money
#             return True
        
#         return False
        
#     def withdraw(self, account, money):
#         """
#         :type account: int
#         :type money: int
#         :rtype: bool
#         """
#         bal = len(self.balance)
#         if 1 <= account < bal and self.balance[account] >= money:
#             self.balance[account] -= money
#             return True
        
#         return False
    
# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
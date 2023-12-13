class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n, ans = len(transactions), [] 
        
        if not n:
            return ans
          
        add, name, time, money, place = [1] * n, [], [], [], []
        
        for tran in transactions:
            tran = tran.split(',')
            name.append(tran[0])
            time.append(int(tran[1]))
            money.append(int(tran[2]))
            place.append(tran[3])
        
        for i in range(n):
            if money[i] > 1000:
                add[i] = False
            
            for j in range(i + 1, n):
                if name[i] == name[j] and abs(time[i] - time[j]) <= 60 and place[i] != place[j]:
                    add[i], add[j] = False, False
            
        for i, val in enumerate(add):
            if not val:
                ans.append(transactions[i])
        
        return ans
                
            
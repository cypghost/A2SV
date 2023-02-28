class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row0 = [1]
        row1 = [1,1]
        
        if rowIndex == 0:
            return row0
        
        elif rowIndex == 1:
            return row1
        
        return self.sum(row1, rowIndex)
    
    def sum(self, row, idx):
        if len(row) == idx + 1:
            return row 
        
        ans = [1]
        
        for index in range(len(row) - 1):
            ans.append(row[index] + row[index + 1])
        
        return self.sum(ans + [1], idx)
        
m, n = map(int, input().split())
 
Rows = []
columns = []
Diag = []
 
for index in range(m):
    Rows.append(list(input()))
    Diag.append([0]*n)
 
for row in range(m):
    for col in range(n):
        if Rows[row].count(Rows[row][col]) > 1:
            Diag[row][col] = "1"
 
for col in zip(*Rows):
    columns.append(col)
    
for col in range(n):
    for row in range(m):
        if columns[col].count(columns[col][row]) > 1:
            Diag[row][col] = "1"
 
answer = ""
 
for row in range(m):
    for col in range(n):
        if Diag[row][col] == 0:
            Diag[row][col] = Rows[row][col]
            answer +=  Rows[row][col]
 
print(answer)

t = int(input())
 
for index in range(t):
    size = list(map(str, input().split()))
        
    if size[0] == size[1]:
        print("=")
    
    elif size[0] == 'M':
        if size[1][-1] == 'L':
            print("<")
        
        else: 
            print(">")
            
    elif size[0][-1] == 'L':
        if size[1][-1] == 'L' and len(size[1]) > len(size[0]):
            print("<")
        
        else:
            print(">")
        
    elif size[0][-1] == 'S':
        if size[1][-1] == 'S' and len(size[1]) > len(size[0]):
            print(">")
        
        else:
            print("<")
        

if __name__ == '__main__':
    N = int(input())
    list = []
    
    for i in range(N):
        commands = input().split()
        command = commands[0]
        
        if command == "insert":
            list.insert(int(commands[1]),int(commands[2]))
            
        elif command == "print":
            print(list)
            
        elif command == "remove":
            list.remove(int(commands[1]))
            
        elif command == "sort":
            list.sort()
            
        elif command == "pop":
            list.pop()
            
        elif command == "append":
            list.append(int(commands[1]))
            
        elif command == "reverse":
            list.reverse()
        

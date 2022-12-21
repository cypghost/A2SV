# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
room = input().split(" ")
'''
{
    key: value
}
'''
rooms = {}
for i in range (len(room)):
    if room[i] not in rooms:
        rooms[room[i]] = 1
    else:
        rooms[room[i]] += 1
    
for key in rooms:
    if rooms[key] == 1:
        print (key)
        break

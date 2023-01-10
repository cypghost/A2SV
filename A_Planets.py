t = int(input())
dict = {}

for index in range(t):
    n, c = map(int, input().split())
    planets = list(map(int, input().split()))
    count = 0
    
    for orbit in set(planets):
        dict[orbit] = planets.count(orbit)
        
        if dict[orbit] > c:
            count += c
        
        else:
            count += dict[orbit]
            
    print(count)
        

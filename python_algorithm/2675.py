num = int(input())

for i in range(num):
    n, s = input().split()
    answer = ''
    
    for j in s:
        answer += int(n) * j
        
    print(answer)
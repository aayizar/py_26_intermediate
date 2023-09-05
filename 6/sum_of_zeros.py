"""
N = int(input())
factorial = 1
sum = 0

for el in range(2, N+1):
    factorial *= el

factorial = str(factorial)
for number in factorial[::-1]:
    if number == '0':
        sum += 1
    else:
        break

print(sum)
"""

def zeros(n):
    five_cnt = 0
    two_cnt = 0
    
    for i in range(2, n + 1):
        number = i
        while number % 2 == 0:
            two_cnt += 1
            number /= 2
            
        number = i
        while number % 5 == 0:
            five_cnt += 1
            number /= 5
    
    return min(five_cnt, two_cnt)
    
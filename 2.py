print('Enter the number below which to find the sum of even fibonacci numbers')
n = int(input())
i = 8
prev = 2
result = 2
while(i < n):
    result = result + i
    currentI = i
    i = (i * 4) + prev
    prev = currentI

    
print('Result is', int(result))
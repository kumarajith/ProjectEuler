def sequenceSum(x):
    return x * (x + 1) / 2
    
print('Enter the number below which to find the sum of multiples of 3 and 5 ')
n = int(input())
n = n-1
result = (3 * sequenceSum(n//3)) + (5 * sequenceSum(n//5)) - (15 * sequenceSum(n//15))
print('Result is', int(result))
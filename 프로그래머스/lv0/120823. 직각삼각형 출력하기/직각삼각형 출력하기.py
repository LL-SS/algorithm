n = int(input())
array = []

for i in range(1, n + 1):
    array.append('*' * i)
    
print(*array, sep='\n')
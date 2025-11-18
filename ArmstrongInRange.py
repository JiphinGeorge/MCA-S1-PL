#Print Armstrong numbers in range (100, 500)

def is_armstrong(n):
    return sum(int(d)**3 for d in str(n)) == n

for num in range(100, 500):
    if is_armstrong(num):
        print(num)

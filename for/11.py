def prime_check(j):
    if j <= 1:
        return False
    for i in range(j):
        if ((i+1 != 1)and(i+1 != j)) and j%(i+1) == 0:
            return False
    return True

for i in range(25,50+1):
    if prime_check(i):
        print(i)

from timelock import timelock_unlock

hexctxt = input("Enter hex puzzle text: ")
t = int(input("Enter number of T operations: "))
n = int(input("Enter the modulus N: "))
ptxt = timelock_unlock(hexctxt, t, n)
print(ptxt)

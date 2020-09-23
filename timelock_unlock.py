from timelock import timelock_unlock

hexctxt = input("Enter hex puzzle text: ")
t = int(input("Enter number of T operations: "))
n = int(input("Enter the modulus N: "))
ctxt = bytes.fromhex(hexctxt)
ptxt = timelock_unlock(ctxt, t, n)
print(ptxt)

from timelock import timelock_lock

psize = 3072
msg = input("Enter message to time lock: ")
t = int(input("Enter number of T operations: "))
ctxt, w, n = timelock_lock(str.encode(msg), t, psize)
print("W key", w)
print("N modulus", n)
ctxt = "".join("{:02x}".format(c) for c in ctxt)
print("Puzzle", ctxt)

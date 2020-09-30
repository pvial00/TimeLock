from Crypto.Util import number

# Time-Lock Puzzle - Rivest, Shamir, Wagner

def genPrimes(psize):
    p = number.getPrime(psize)
    q = number.getPrime(psize)
    while q == p:
        q = number.getPrime(psize)
    return p, q

def timelock_lock(msg, t, psize=3072, n=None, p=None, q=None):
    if n == None or p == None or q == None:
        p, q = genPrimes(psize)
        n = p * q
    m = number.bytes_to_long(msg)
    phi = (p - 1) * (q - 1)
    u = pow(2, t, phi)
    w = pow(2, u, n)
    ctxt = m ^ w
    return number.long_to_bytes(ctxt), w, n

def timelock_unlock_master_key(hexctxt, w):
    ctxt = bytes.fromhex(hexctxt)
    m = number.bytes_to_long(ctxt)
    ptxt = m ^ int(w)
    return number.long_to_bytes(ptxt)

def timelock_unlock(hexctxt, t, n):
    ctxt = bytes.fromhex(hexctxt)
    c = number.bytes_to_long(ctxt)
    a = 2
    T = 0
    while True:
        T += 1
        a = pow(2, pow(2, T), n)
        if T == t:
            break
    m = c ^ a
    return number.long_to_bytes(m)

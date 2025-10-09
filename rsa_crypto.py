from Crypto.Util import number

class RSA:
    def Grsa(self, l, e):
        p = number.getPrime(l)
        while number.GCD(p-1, e) != 1:
            p = number.getPrime(l)
        
        q = number.getPrime(l)
        while number.GCD(q-1, e) != 1 or p == q:
            q = number.getPrime(l)
        
        phi = (p-1) * (q-1)
        d = number.inverse(e, phi)
        n = p * q
        
        pk = (n, e)
        sk = (n, d)
        return sk, pk

    def Frsa(self, pk, x):
        (n, e) = pk
        return pow(x, e, n)
    
    def Irsa(self, sk, y):
        (n, d) = sk
        return pow(y, d, n)
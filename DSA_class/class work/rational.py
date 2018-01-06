from fractions import gcd
class rational:
    def __init__(self,num,den):
        if (den == 0):
            return "No zero"
        norm = int(gcd(num,den))
        self._num = num/norm
        self._den = den/norm
    def __add__(self,other):
        GCD = gcd(self._den,other._den)
        numerator = self._num*GCD/self._den + other._num*GCD/other._den
        denominator = GCD
        ans = rational(numerator,denominator)
        return ans
    def __str__(self):
        if (self._den == 1):
            return str(self._num)
        else:
            return str(self._num)+'/'+str(self._den)

print(rational(10,30) + rational(40,30))

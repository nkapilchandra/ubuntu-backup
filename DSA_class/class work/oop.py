class ComplexNumber:
    """docstring for ComplexNumber."""
    def __init__(self,x,y):
        self._real = x
        self._imag = y
    def __add__(self,other):
        self._real += other._real
        self._imag += other._imag
        return self
    def __mul__(self,other):
        new = ComplexNumber(0,0)
        new._real = (self._real*other._real - self._imag*other._imag)
        new._imag = (self._imag*other._real + self._real*other._imag)
        return new
    def get_real(self):
        return self._real
    def get_imag(self):
        return self._imag
    def __repr__(self):
        return str(self._real) +' + i'+ str(self._imag)

z1 = ComplexNumber(1,1)
z2 = ComplexNumber(-2,-2)
z3 = ComplexNumber(0.5,0)

print(z1 + z2* z3)

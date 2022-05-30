class ComplexNumber:
    def __init__(self, real: float, im: float):
        self.real = real
        self.im = im

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.im + other.im)

    def __str__(self):
        if self.im == 0:
            return '%.2f' % self.real
        if self.real == 0:
            return '%.2fi' % self.im
        if self.im < 0:
            return '%.2f - %.2fi' % (self.real, -self.im)
        else:
            return '%.2f + %.2fi' % (self.real, self.im)

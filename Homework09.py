def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num // cmmn, new_den // cmmn)

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

class MixedFraction(Fraction):
    
    def __init__(self, fraction):
        Fraction.__init__(self, fraction.num, fraction.den)

    def __add__(self, other_fraction):
        return MixedFraction(Fraction.__add__(self, other_fraction))

    def __str__(self):
        cmmn = gcd(self.num, self.den)
        new_num = self.num//cmmn
        new_den = self.den//cmmn
        whole = 0
        if new_num > 0:
            while new_num >= new_den:
                new_num = new_num - new_den
                whole = whole + 1
            return "{:d}_({:d}/{:d})".format(whole, new_num, new_den)
        elif new_num < 0:
            new_num = -1*new_num
            while new_num >= new_den:
                new_num = new_num - new_den
                whole = whole + 1
            return "-{:d}_({:d}/{:d})".format(whole, new_num, new_den)
        else:
            return "{:d}_({:d}/{:d})".format(whole, new_num, new_den)
    
def main():
    
    print("*" * 30 + "\nPrinting main() source code:\n" + "*" * 30)
    import inspect
    print(str(inspect.getsource(main)))
    print("*" * 30 + "\nPrinting main() source output:\n" + "*" * 30)
    
    f1 = Fraction(1, 2)
    f2 = Fraction(-7, 3)
    f3 = Fraction(-1, 4)
    f4 = Fraction(21, 5)
    f5 = f1 + f2 + f3 + f4

    print("f1: " + str(f1))
    print("f2: " + str(f2))
    print("f3: " + str(f3))
    print("f4: " + str(f4))
    print("f5: " + str(f5))
    print("isinstance(f5, Fraction): " + str(isinstance(f5, Fraction)))
    print("isinstance(f5, MixedFraction): " + str(isinstance(f5, MixedFraction)))
    
    m1 = MixedFraction(f1)
    m2 = MixedFraction(f2)
    m3 = MixedFraction(f3)
    m4 = MixedFraction(f4)
    m5 = m1 + m2 + m3 + m4

    print("m1: " + str(m1))
    print("m2: " + str(m2))
    print("m3: " + str(m3))
    print("m4: " + str(m4))
    print("m5: " + str(m5))
    print("isinstance(m5, Fraction): " + str(isinstance(m5, Fraction)))
    print("isinstance(m5, MixedFraction): " + str(isinstance(m5, MixedFraction)))

    print("(f5==m5) : " + str(f5==m5))
    

if __name__ == "__main__":
    main()

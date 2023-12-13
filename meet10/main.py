import math
class Kalkulator:

    def __init__(self, x, y):
        self.A = x
        self.B = y
        print("A=" + str(x) + ", B=" + str(y))

    def tambah(self):
        self.hasil = self.A + self.B
        print("A+B=" + str(self.hasil))

    def kurang(self):
        self.hasil = self.A - self.B
        print("A-B=" + str(self.hasil))

    def kali(self):
        self.hasil = self.A * self.B
        print("A*B=" + str(self.hasil))

    def bagi(self):
        if self.B == 0:
            print("Pembagian dengan nol")
        else:
            self.hasil = self.A / self.B
            print("A/B=" + str(self.hasil))
    def pangkat(self):
        self.hasil = self.A ** self.B
        print("A^B = "+str(self.hasil))

    def factorial(self):
        self.hasil = math.factorial(self.A)
        print(f"A! = {self.hasil}")
    def modulus(self):
        self.hasil = self.A % self.B
        print(f"A % B = {self.hasil}")

print("--==Object Pertama==--")# Membuat objek pertama
object1 = Kalkulator(5, 2)
object1.tambah()
object1.kurang()
object1.kali()
object1.bagi()
object1.pangkat()
object1.factorial()
object1.modulus()
print("--==Object Kedua==--")# Membuat objek kedua
object2 = Kalkulator(2, 0)
object2.bagi()
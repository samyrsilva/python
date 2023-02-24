num1 = int(input("digite valor"))
num2 = int(input("digite valor"))

class calculadora:
    def __init__(self, num1, num2):
        self.vl_a = num1
        self.vl_b = num2
    def soma(self):
        return  self.vl_a + self.vl_b

    def subtr(self):
        return self.vl_a - self.vl_b

    def div (self):
        return self.vl_a / self.vl_b
    
    def mult(self):
        return self.vl_a * self.vl_b

calculadora = calculadora (num1, num2)

print(calculadora.vl_a)
print(calculadora.vl_b)
print(calculadora.soma())
print(calculadora.subtr())
print(calculadora.div())
print(calculadora.mult())
# print(soma(1, 3))
# print(soma(2, 5))
#
# print(mult(2, 4))
# print(mult(8, 4))
#
# print(div(5, 6))

calculadora = calculadora

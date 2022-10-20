class Aritmetica:
    def __init__(self, operadorA, operadorB):
        self.operadorA = operadorA
        self.operadorB = operadorB
       
    def sumar(self):
        return self.operadorA + self.operadorB
        
    def restar(self):
        return self.operadorA - self.operadorB
        
    def multiplicar(self):
        return self.operadorA * self.operadorB
    
    def dividir (self):
        return self.operadorA / self.operadorB
        
Aritmetica1 = Aritmetica (5,6)

print(f'la suma es: {Aritmetica1.sumar()}')
print(f'la resta es: {Aritmetica1.restar()}')
print(f'la multiplicacion es: {Aritmetica1.multiplicar()}')
print(f'la division es: {Aritmetica1.dividir()}')
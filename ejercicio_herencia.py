class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return ' color: ' + self.color + ', ruedas: ' + str(self.ruedas)
        
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return super().__str__(', velocidad: ' + str(self.velocidad))
        
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ', tipo: ' + self.tipo
    
Bicicleta1 = Bicicleta ("rojo", 55, "AWA")
print ( Bicicleta1)
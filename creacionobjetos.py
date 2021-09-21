print("Hola mundo OPP   POO")

class carro():
    
    def __init__(self, name):
        self.nombre = name
    
    def acelerar(self):
        print("Estoy acelerando")
        
    def transportar(self, per):
        print("Estoy trnasportando", per, "personas", self.nombre)
        
bmw01 = carro("bmw01") #crea el objeto
bmw01.acelerar()
bmw01.transportar(4)

mazda01 = carro("mazda01") #crea el objeto
mazda01.transportar(8)


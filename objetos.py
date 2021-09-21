class computador():
    
    def iniciar(self):
        print("Iniciando...")
        
    def apagar(self):
        print("apagando...")
        
    def internet(self):
        print("|ingresando a internet|")
        
windows = computador()

def PC():
    while True:
        PC = input("¿Que desea hacer?")

        if PC == "iniciar":
            windows.iniciar()
        elif PC == "internet":
            windows.internet()
        elif PC == "apagar":
            windows.apagar()
            break
            
PC()
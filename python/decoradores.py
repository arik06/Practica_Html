#se ingresa una funcion y da  de vuelta una funcion  mejorada

def anuncio (f):
    def wrapper():
        print("Anuncio")
        f()
        print("Anuncioxd")
        return wrapper
                    
@anuncio 
def hello():
                    print("Hola")
                    hello()
import Pyro5.api
import math

@Pyro5.api.expose
class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b
    
    def raiz_quadrada(self, a):
        if a < 0:
            raise ValueError("Não é possível calcular raiz de número negativo")
        return math.sqrt(a)
    
    def exponenciacao(self, base, expoente):
        return base ** expoente

def main():
    calculadora = Calculadora()
    
    daemon = Pyro5.api.Daemon()

    try:
        ns = Pyro5.api.locate_ns()
    except Pyro5.errors.NamingError:
        print("Erro: Não foi possível localizar o nameserver.")
        return

    
    uri = daemon.register(calculadora)
    ns.register("calculadora.distribuida", uri)

    print("Servidor da calculadora ouvindo...")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
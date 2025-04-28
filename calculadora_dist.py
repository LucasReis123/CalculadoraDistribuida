from xmlrpc.server import SimpleXMLRPCServer
import math

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
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Servidor da calculadora ouvindo na porta 8000...")
    
    calculadora = Calculadora()
    server.register_instance(calculadora)
    
    server.register_function(calculadora.soma, 'soma')
    server.register_function(calculadora.subtracao, 'subtracao')
    server.register_function(calculadora.multiplicacao, 'multiplicacao')
    server.register_function(calculadora.divisao, 'divisao')
    server.register_function(calculadora.raiz_quadrada, 'raiz_quadrada')
    server.register_function(calculadora.exponenciacao, 'exponenciacao')
    
    server.serve_forever()

if __name__ == "__main__":
    main()
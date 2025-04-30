import Pyro5.api
import os

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=== Calculadora Distribuída ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Raiz Quadrada")
    print("6. Exponenciação")
    print("0. SAIR")
    return input("Escolha uma operação (0-6): ")

def main():
    # Localiza o nameserver Pyro5
    ns = Pyro5.api.locate_ns()
    
    # Obtém a URI do servidor da calculadora
    calculadora_uri = ns.lookup("calculadora.distribuida")  # Nome registrado no servidor Pyro5

    # Conecta ao servidor e cria um proxy para o objeto remoto
    calculadora = Pyro5.api.Proxy(calculadora_uri)

    while True:
        opcao = mostrar_menu()
        
        if opcao == '0':
            print("Saindo...")
            break
        
        try:
            if opcao == '1':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                resultado = calculadora.soma(a, b)
                print(f"Resultado: {a} + {b} = {resultado}")
                
            elif opcao == '2':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                resultado = calculadora.subtracao(a, b)
                print(f"Resultado: {a} - {b} = {resultado}")
                
            elif opcao == '3':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                resultado = calculadora.multiplicacao(a, b)
                print(f"Resultado: {a} * {b} = {resultado}")
                
            elif opcao == '4':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                resultado = calculadora.divisao(a, b)
                print(f"Resultado: {a} / {b} = {resultado}")
                
            elif opcao == '5':
                a = float(input("Digite o número: "))
                resultado = calculadora.raiz_quadrada(a)
                print(f"Resultado: √{a} = {resultado}")
                
            elif opcao == '6':
                base = float(input("Digite a base: "))
                expoente = float(input("Digite o expoente: "))
                resultado = calculadora.exponenciacao(base, expoente)
                print(f"Resultado: {base}^{expoente} = {resultado}")
                
            else:
                print("Opção inválida! Tente novamente.")
                
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
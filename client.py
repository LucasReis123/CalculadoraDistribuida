import xmlrpc.client

def mostrar_menu():
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
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    
    while True:
        opcao = mostrar_menu()
        
        if opcao == '0':
            print("Saindo...")
            break
        
        try:
            if opcao == '1':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                resultado = proxy.soma(a, b)
                print(f"Resultado: {a} + {b} = {resultado}")
                
            elif opcao == '2':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                resultado = proxy.subtracao(a, b)
                print(f"Resultado: {a} - {b} = {resultado}")
                
            elif opcao == '3':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                resultado = proxy.multiplicacao(a, b)
                print(f"Resultado: {a} * {b} = {resultado}")
                
            elif opcao == '4':
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                resultado = proxy.divisao(a, b)
                print(f"Resultado: {a} / {b} = {resultado}")
                
            elif opcao == '5':
                a = float(input("Digite o número: "))
                resultado = proxy.raiz_quadrada(a)
                print(f"Resultado: √{a} = {resultado}")
                
            elif opcao == '6':
                base = float(input("Digite a base: "))
                expoente = float(input("Digite o expoente: "))
                resultado = proxy.exponenciacao(base, expoente)
                print(f"Resultado: {base}^{expoente} = {resultado}")
                
            else:
                print("Opção inválida! Tente novamente.")
                
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
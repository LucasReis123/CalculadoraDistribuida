
# Calculadora Distribuída com Pyro5 (Python Remote Objects)

Este projeto implementa uma **aplicação distribuída de calculadora** utilizando a biblioteca **Pyro5**, que permite a chamada remota de métodos (semelhante ao Java RMI, porém em Python). A aplicação é composta por dois componentes principais:

- **Servidor:** expõe os métodos da calculadora para serem utilizados remotamente.
- **Cliente:** conecta-se ao servidor, envia comandos e exibe os resultados das operações.

## Funcionalidades

A calculadora distribuída implementa os seguintes métodos:

1. **Soma** de dois números
2. **Subtração** de dois números
3. **Multiplicação** de dois números
4. **Divisão** de dois números (com tratamento de divisão por zero)
5. **Raiz quadrada** de um número (com validação de número negativo)
6. **Exponenciação** (base elevada a um expoente)

## Requisitos

- Biblioteca Pyro5 instalada

Você pode instalar a biblioteca Pyro5 com o seguinte comando:

```bash
pip install Pyro5
```

## Como Executar

### 1. Inicie o **Name Server** do Pyro5

O **Name Server** é responsável por gerenciar os nomes registrados de objetos remotos. **Esse passo é obrigatório** e deve ser feito antes de iniciar o servidor.

Abra um terminal e execute:

```bash
python3 -m Pyro5.nameserver
```

Esse comando iniciará o name server na porta padrão (9090). **Deixe essa janela aberta** enquanto executa o servidor e o cliente.

---

### 2. Execute o **Servidor da Calculadora**

Em um **novo terminal**, execute o arquivo do servidor:

```bash
python3 calculadora_dist.py
```
---

### 3. Execute o **Cliente da Calculadora**

Em outro terminal, execute o cliente:

```bash
python3 client.py
```

Você verá o seguinte menu:

```
=== Calculadora Distribuída ===
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Raiz Quadrada
6. Exponenciação
0. SAIR
```

Basta escolher uma opção e fornecer os valores solicitados. O cliente irá se comunicar com o servidor, realizar a operação e exibir o resultado.

---

## Como Funciona

- O servidor define uma classe `Calculadora` com métodos que são **expostos remotamente** usando o decorador `@Pyro5.api.expose`.
- Essa classe é registrada no **Name Server** com o nome `"calculadora.distribuida"`.
- O cliente se conecta ao **Name Server**, busca a URI da calculadora e cria um **proxy remoto**.
- Todas as chamadas feitas no cliente (`calculadora.soma(...)`, etc.) são **executadas remotamente** no servidor.

---

## Tratamento de Erros

- **Divisão por zero**: o servidor lança uma exceção com a mensagem `"Não é possível dividir por zero"`.
- **Raiz quadrada de número negativo**: o servidor lança uma exceção com a mensagem `"Não é possível calcular raiz de número negativo"`.
- O cliente printa essas exceções.

---

## Estrutura dos Arquivos

- `calculadora_dist.py`: código do servidor da calculadora (com os métodos expostos via Pyro5).
- `client.py`: código do cliente que interage com o usuário e com o servidor.

---

## Exemplo de Execução

```
=== Calculadora Distribuída ===
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Raiz Quadrada
6. Exponenciação
0. SAIR
Escolha uma operação (0-6): 1
Digite o primeiro número: 10
Digite o segundo número: 5
Resultado: 10.0 + 5.0 = 15.0
```

---

## Encerrando

Para encerrar a aplicação:

1. Digite `0` no menu do cliente.
2. Feche o terminal do servidor.
3. Finalize o processo do `nameserver` com `Ctrl+C`.

---

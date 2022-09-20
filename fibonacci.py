'''
    Algoritmos para o cálculo do n-ésimo número de Fibonacci 
    inteiro não negativo  
'''

## ==================================================================
def main():
    print("TESTES DAS FUNÇÔES")
    
    print("fibonacciR:")
    print(f"Fibonacci(5) = {fibonacciR(5)} -> Resposta = 5")
    print(f"Fibonacci(10) = {fibonacciR(10)} -> Resposta = 55")
    print(f"Fibonacci(20) = {fibonacciR(20)} -> Resposta = 6765")
    print(f"Fibonacci(30) = {fibonacciR(30)} -> Resposta = 832040")
    print(f"Fibonacci(40) = {fibonacciR(40)} -> Resposta = 102334155")
    
    print("fibonacciI:")
    print(f"Fibonacci(5) = {fibonacciI(5)} -> Resposta = 5")
    print(f"Fibonacci(10) = {fibonacciI(10)} -> Resposta = 55")
    print(f"Fibonacci(20) = {fibonacciI(20)} -> Resposta = 6765")
    print(f"Fibonacci(30) = {fibonacciI(30)} -> Resposta = 832040")
    print(f"Fibonacci(40) = {fibonacciI(40)} -> Resposta = 102334155")
    
## ==================================================================

def fibonacciR(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma recursiva.
    Retorna o valor calculado.

    Exemplos:
    fibonacciR(5) = 5
    fibonacciR(10) = 55
    fibonacciR(20) = 6765
    fibonacciR(30) = 832040
    fibonacciR(40) = 102334155
    '''
    # casos base:
    if n == 0 or n ==1:
        return n
    #if n == 1:
    #   return 1:
    else:
        return fibonacciR(n-1) + fibonacciR(n-2)


## ==================================================================

def fibonacciI(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma iterativa.
    Retorna o valor calculado.
    '''
    soma = 0
    anterior = 0
    for i in range(n+1):
        if i == 1:
            soma += 1
        else:
            soma += anterior
            anterior = soma - anterior
    
    return soma


if  __name__ == '__main__':
    main()
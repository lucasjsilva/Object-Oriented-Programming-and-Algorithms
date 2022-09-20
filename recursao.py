'''
    Escrtita de funções recursivas 
'''

## ==================================================================

def main():

    print("Testes das funções recursivas \n")
    
    lst1 = [1,2,3,4,5]
    lst2 = [-2,14,-4,8]
    lst3 = []
    lst4 = [5,5,5,5,5]
    lst5 = [-10,-20,-30,-40,-50]
    
    print(f"O maior inteiro de {lst1} é: {maxR(lst1)} --> Resposta = 5")
    print(f"O maior inteiro de {lst2} é: {maxR(lst2)} --> Resposta = 14")
    print(f"O maior inteiro de {lst3} é: {maxR(lst3)} --> Resposta = None")
    print(f"O maior inteiro de {lst4} é: {maxR(lst4)} --> Resposta = 5")
    print(f"O maior inteiro de {lst5} é: {maxR(lst5)} --> Resposta = -10")
    print(f"A soma de {lst1} é: {somaR(lst1)} --> Resposta = 15")
    print(f"A soma de {lst2} é: {somaR(lst2)} --> Resposta = 16")
    print(f"A soma de {lst3} é: {somaR(lst3)} --> Resposta = 0")
    print(f"A soma de {lst4} é: {somaR(lst4)} --> Resposta = 25")
    print(f"A soma de {lst5} é: {somaR(lst5)} --> Resposta = -150")

## ------------------------------------------------------------------

def maxR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna o valor do maior elemento.
        Exemplos: 
        - para a entrada [12, 15, 7], a funcao deve retornar 15.
        - para a entrada [51], a funcao deve retornar 51.
        - para a entrada [], a funcao deve retornar None.

        OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
        não use a função nativa max() do Python para resolver esse exercício.
    '''
    if len(lista) == 0:
        return None
    if len(lista) == 1:
        return lista[0]
    else:
        return max(lista[0],maxR(lista[1:]))
    

    #print("Vixe! ainda não fiz a função maxR.")

## ------------------------------------------------------------------

def somaR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna a soma de todos os elementos da lista.
        Exemplo: 
        - para a entrada [12, -15, 7], a funcao deve retornar 4.
        - para a entrada [51], a funcao deve retornar 51.
        - para a entrada [], a funcao deve retornar 0 (zero).

        OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
        não use a função nativa sum() do Python para resolver esse exercício.
    '''
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somaR(lista[1:])


## ------------------------------------------------------------------

if __name__ == '__main__':
    main()
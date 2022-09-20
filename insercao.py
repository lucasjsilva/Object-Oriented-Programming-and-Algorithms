'''
    Diferentes algoritmos de inserção 
'''

def main():

    print("Testes - ordenação por inserção")
    print("FUNÇÃO INSIRA_ULTIMO")
    print(f"primeiro teste, lista [4,7,11,5,3]: {insira_ultimo([4,7,11,5,3],4)}")
    print(f"primeiro teste, lista [4,5,7,11,3]: {insira_ultimo([4,5,7,11,3],5)}")
    
    print("FUNÇÃO ORDENE_POR_INSERÇÃO")
    print(ordene_por_insercao([4, 7, 5, 3]))

## ==================================================================

def insira_ultimo(seq, n):
    ''' (list, int) -> None

    Essa função é a base para o algoritmo de ordenação 
    por inserção, que veremos em uma próxima aula e 
    não se trata de um algoritmo completo de ordenação.

    Essa função considerar apenas a porção da lista seq 
    no intervalo [0:n].

    A ideia é visitar cada elemento, a partir do fim da 
    porção, ou seja, do elemento de índice n-1.
    Caso o elemento anterior seja maior, os elementos são
    trocados de posição, fazendo o elemento visitado "descer"
    na lista. A varredura deve persistir enquanto o elemento 
    visitado for menor que o seu anterior.

    Por exemplo,  para seq = [4, 7, 11, 5, 3] e n = 3 a
    função não precisa fazer nada pois o elemento anterior
    ao 11 já é menor. 

    Para seq = [4, 7, 11, 5, 3] e n = 4 a
    função deve deslocar o 5 até que seq se torne 
    [4, 5, 7, 11, 3]. 

    Outro exemplo, para seq = [4, 5, 7, 11, 3] e n = 5 a
    função deve deslocar o 3 até que seq se torne 
    [3, 4, 5, 7, 11]. 

    DICA: não use outras listas, nem fatias. Basta
    varrer seq, comparar com seu vizinho anterior
    e trocar enquanto necessário.

    '''
    # primerio eu varro seq
    ind = n-1
    anterior = ind - 1
    while anterior >= 0:
        if seq[ind] < seq[anterior]:
            guarda = seq[ind]
            seq[ind] = seq[anterior]
            seq[anterior] = guarda
            ind -= 1
            anterior = ind - 1
        if seq[ind] >= seq[anterior]:
            return None
    
## ==================================================================

def ordene_por_insercao(seq):
    ''' (list) -> None

    A ideia de ordenação por inserção (insertion sort)
    é considerar porções da lista, a partir de 2 elementos até n.
    Para cada porção, apenas o último elemento precisa ser 
    deslocado até sua posição correta.

    Exemplo para a lista [4, 7, 5, 3]
    - inicio com a porção da lista de tamanho 2 contendo [4, 7, ? , ?]. 
        O último elemento já está na posição correta. 
    - a ordenação continua com a porção de tamanho 3 com [4, 7, 5, ?]
        O último elemento da porção, o 5, precisa ser deslocado até
        sua posição final [4, 5, 7, ?]
    - a ordenação continua com a porção de tamanho 4, agora com 
        [4, 5, 7, 3]. O último elemento da porção, o 3, precisa ser
        deslocado até sua posição final [3, 4, 5, 7].
    - fim, pois já tratamos todas as porções até o tamanho n.

    O que você deve fazer: 

    A função recebe uma sequência de números em ordem aleatória. 
    e retorna None. Ao terminar, seq deve estar em ordem
    crescente aplicando a ideia de ordenação por inserção.

    Essa função DEVE usar a função insira_ultimo().

    '''
    for i in range(len(seq) - 1):
        j = i+1 # vai percorrer as sub listas
        while j > 0:
            if seq[j] < seq[j-1]:
                guarda = seq[j]
                seq[j] = seq[j-1]
                seq[j-1] = guarda
                j-=1
            else:
                j = -1

## ==================================================================

if __name__ == '__main__':
    main()

## ==================================================================

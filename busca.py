'''
    Diferentes algoritmos de busca 
'''

import numpy as np

## ==================================================================
def main():
    print("TESTES DAS FUNÇÔES:")
    print("===============================")
    
    # teste busca sequencial
    print ("TESTE BUSCA SEQUÊNCIAL:")
    seq1 = [4, 7, 8, 3, 2, 0, 1, 5, 9, 6]
    
    bs1 = busca_sequencial(seq1, 0)
    bs2 = busca_sequencial(seq1, 8)
    bs3 = busca_sequencial(seq1, -1)
    print(f"A sequênica seq1 é: {seq1}")
    print(f"busca_sequencial(seq1, 0) retorna {bs1} -> resposta: 5")
    print(f"busca_sequencial(seq1, 8) retorna {bs2} -> resposta: 2")
    print(f"busca_sequencial(seq1, -1) retorna {bs3} -> resposta: None")
    
    # teste busca ordenanda
    print("===============================")
    print ("TESTE BUSCA ORDENADA:")
    seq2 = [2, 3, 4, 5, 6, 7, 8, 9]
    
    bo1 = busca_sequencial_em_lista_ordenada(seq2, 0)
    bo2 = busca_sequencial_em_lista_ordenada(seq2, 8)
    bo3 = busca_sequencial_em_lista_ordenada(seq2, -1)
    print(f"A sequênica seq1 é: {seq2}")
    print(f"busca_ordenada(seq2, 0) retorna {bo1} -> resposta: None")
    print(f"busca_ordenada(seq2, 8) retorna {bo2} -> resposta: 6")
    print(f"busca_ordenada(seq2, -1) retorna {bo3} -> resposta: None")
    
    # teste busca binomial recursiva
    print("===============================")
    print ("TESTE BUSCA BINOMIAL:")
    seq2 = [2, 3, 4, 5, 6, 7, 8, 9]
    
    bb1 = busca_binariaR(seq2, 0)
    bb2 = busca_binariaR(seq2, 8)
    bb3 = busca_binariaR(seq2, -1)
    print(f"A sequênica seq1 é: {seq2}")
    print(f"busca_binomial(seq2, 0) retorna {bb1} -> resposta: None")
    print(f"busca_binomial(seq2, 8) retorna {bb2} -> resposta: 6")
    print(f"busca_binomial(seq2, -1) retorna {bb3} -> resposta: None")
    
    

## ==================================================================

def busca_sequencial( seq, item ):
    ''' (lista, obj) -> int ou None

        Recebe uma lista seq e um elemento obj. 
        Caso obj esteja na lista, devolve o índice da ocorrência de 
        obj em seq. Você pode assumir que todos os itens são
        diferentes.
        Caso obj não esteja na lista, então a função retorna None.

        OBS: esse é um exercício muito simples para que possamos
        ver a diferença desse algoritmo com os demais. Por isso,
        não use o método index.

        Pré condição: a lista seq não está ordenada.

        Exemplos:

        para seq = [4, 7, 8, 3, 2, 0, 1, 5, 9, 6] então:

        > busca_sequencial( seq, 0) retorna 5
        > busca_sequencial( seq, 8) retorna 2
        > busca_sequencial( seq, -1) retorna None

    '''
    # escreva sua solução
    contador = 0
    for i in seq:
        if i == item:
            return contador
        contador +=1
    return None

## ==================================================================

def busca_sequencial_em_lista_ordenada( seq, item ):
    ''' (lista, obj) -> int ou None

        Recebe uma lista seq em ordem crescente e um elemento obj. 
        Caso obj esteja na lista, devolve o índice da ocorrência de 
        obj em seq. Você pode assumir que todos os itens são
        diferentes.
        
        Caso obj não esteja na lista, então a função retorna None.

        Observe que dependendo do sentido da varredura da lista 
        ordenada, só é necessário percorrer enquanto os itens 
        forem maiores ou menores que o obj.

        Pré condição: a lista seq está ordenada em ordem crescente.

        Exemplos:

        para seq = [2, 3, 4, 5, 6, 7, 8, 9] então

        > busca_sequencial_em_lista_ordenada( seq, 0) retorna None
        > busca_sequencial_em_lista_ordenada( seq, 8) retorna 6
        > busca_sequencial_em_lista_ordenada( seq, -1) retorna None

    '''
    # escreva sua solução
    # analiso se o item é maior ou menor que o elemento do meio
    if item <= seq[len(seq)//2]:
        i = len(seq)//2
        while i >= 0:
            if i == seq[len(seq)//2]:
                return i
            i -= 1
        return None
    if item >= seq[len(seq)//2]:
        i = len(seq)//2
        while i <= len(seq):
            if i == seq[len(seq)//2]:
                return i
            i += 1
        return None

## ==================================================================

def busca_binariaR( seq, item ):
    ''' (lista, obj) -> int ou None

        interface para a busca binária recursiva com esq e dir.
        Esq e dir indicam os índices da porção da lista onde 
        item deve ser procurado.

        Exemplos:

        para seq = [2, 3, 4, 5, 6, 7, 8, 9] então

        > busca_binariaR( seq, 0) retorna None
        > busca_binariaR( seq, 8) retorna 6
        > busca_binariaR( seq, -1) retorna None

        Não modifique essa função.
    '''

    esq = 0
    dir = len(seq)
    return busca_binariaRED(seq, item, esq, dir)

## ==================================================================

def busca_binariaRED( seq, item, esq, dir ):
    ''' (lista, obj, int, int) -> int ou None

        A ideia de busca binária em sequencia ordenada é testar o meio
        da porção da lista delimitada por [esq : dir].

        Implemente a seguinte ideia recursiva:
        - Se o intervalo for nulo, retorna None. 
        
        - Se o item de seq no meio do intervalo for o elemento procurado, 
        retorna esse índice do meio. 
        
        - Caso contrário, se o meio for maior que o procurado, então
        a busca deve continuar recursivamente na metade menor dada por [esq:meio].
        
        - Caso contrário, a busca deve continuar na outra metade (maior) do
        intervalo.

    '''
    # escreva sua solução
    meio = (dir+esq)//2
    # casos base:
    
    # caso 1 - intervalo nulo
    if len(seq[esq:dir])== 0:
       return None
    # caso 2 - valor no meio é o valor procurado
    if item == seq[meio]:
        return meio
    
    # casos recursivos
    if item > seq[meio]:
        return busca_binariaRED(seq, item, meio, dir) 
    if item < seq[meio]:
        return busca_binariaRED(seq, item, esq, meio) 

## ==================================================================
if __name__ == "__main__":
    main()

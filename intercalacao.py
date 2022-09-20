'''
         
'''

## ==================================================================
def main():
    
    print("Testes - ordenação por intercalação")

    # escreva seus testes
    l1 = [7, 11, 56]
    l2 = [-5, 7, 99, 104]
    l3 = [-4, -3, -1, 1, 3, 4]
    l4 = [-2]
    l5 = []
    l6 = [10, 20, 30, 40, 50, 60]
    l7 = []
    l8 = [2]
    
    
    print(f" Teste 1 com listas {l1} e {l2} -> {intercale_seqs(l1, l2)}")
    print(f" Teste 2 com listas {l1} e {l3} -> {intercale_seqs(l1, l3)}")
    print(f" Teste 3 com listas {l4} e {l5} -> {intercale_seqs(l4, l5)}")
    print(f" Teste 4 com listas {l1} e {l5} -> {intercale_seqs(l1, l5)}")
    print(f" Teste 5 com listas {l3} e {l4} -> {intercale_seqs(l3, l4)}")
    print(f" Teste 6 com listas {l2} e {l6} -> {intercale_seqs(l2, l6)}")
    print(f" Teste 7 com listas {l1} e {l6} -> {intercale_seqs(l1, l6)}")
    print(f" Teste 8 com listas {l5} e {l7} -> {intercale_seqs(l5, l7)}")
    print(f" Teste 9 com listas {l4} e {l8} -> {intercale_seqs(l4, l8)}")
    print(f" Teste 10 com listas {l1} e {l7} -> {intercale_seqs(l1, l7)}")
    
## ------------------------------------------------------------------

def intercale_seqs(seq1, seq2):
    ''' (list, list) -> list

    Recebe seq1 e seq2, duas listas tal que:

        - seq1 é crescente com n1 >= 0 elementos e
        - seq2 é crescente com n2 >= 0 elementos
        
    Retorna uma lista com n1+n2 elementos, contendo
    os elementos de seq1 e seq2 em ordem crescente.

    Exemplo para 
        seq1 = [7, 11, 56] e 
        seq2 = [-5, 7, 99, 104]
    
    a função deve retornar a lista:
        [-5, 7, 7, 11, 56, 99, 104]
    '''
    
    # primeiro eu crio uma nova lista com tamanho da concatenação de ambas
    lista = [0]*(len(seq1) + len(seq2))
    cont1 = 0
    cont2 = 0
    i =0
    while cont1 < len(seq1) and cont2 < len(seq2):
        if seq1[cont1] < seq2[cont2]:
            lista[i] = seq1[cont1]
            cont1 += 1
        else:
            lista[i] = seq2[cont2]
            cont2 += 1
        i += 1
        
    if cont1 < len(seq1):
        while cont1 < len(seq1):
            lista[i] = seq1[cont1]
            cont1 += 1
            i += 1
    else:
        while cont2 < len(seq2):
            lista[i] = seq2[cont2]
            cont2 += 1
            i += 1
       
    return lista
    

#--------------------------------------------
if __name__ == '__main__':
    main()
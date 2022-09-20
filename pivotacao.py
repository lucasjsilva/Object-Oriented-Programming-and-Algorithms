'''
    (list) -> int

    Recebe uma lista seq com n>0 elementos 
    e rearranja seus elementos para que o pivô, 
    o último elemento da lista,
    esteja na posição "ordenada" com relação aos demais 
    elementos, ou seja, todos os elementos menores fiquem
    a esquerda e todos os maiores fiquem a direita do pivô.

    Retorna um índice m tal que

        seq[:m] <= seq[m] < seq[m+1:]
    
    Exemplos:
    In [1] seq = [5, 7, 4, 3, 8, 6]
    In [2] m = pivote_seq(seq)
    In [3] m
    3
    In [4] seq
    [5, 4, 3, 6, 8, 7]

    ...

    In [11] seq = [6, 7, 5, 3, 8, 4]
    In [12] m = pivote_seq(seq)
    In [13] m
    1
    In [14] seq
    In [3, 4, 5, 6, 8, 7] 
'''

## ==================================================================
def main():
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas de tamanho mínimo, em ordem crescente,
        decrescente, etc.
    '''
    print("Testes - ordenação por pivotação")
    
    s1 = [5,7,4,3,8,6]
    print(f"teste 1: em {s1} a posição é: {pivote_seq(s1)} -> resposta = 3")
    s2 = [40,21,10]
    s3 = [21,40,10]
    s4 = [18,9]
    s5 = [12]
    s6 = [40,70,20,80]
    s7 = [70,43,11,59,22,60,33]
    s8 = [1,3,5,7,9,11]
    s9 = [10,8,6,4,2]
    s10 = [-2,5,8,-4,-3,1]
    print(f"teste 2: em {s2} a posição é: {pivote_seq(s2)} -> resposta = 0")
    print(f"teste 3: em {s3} a posição é: {pivote_seq(s3)} -> resposta = 0")
    print(f"teste 4: em {s4} a posição é: {pivote_seq(s4)} -> resposta = 0")
    print(f"teste 5: em {s5} a posição é: {pivote_seq(s5)} -> resposta = 0")
    print(f"teste 6: em {s6} a posição é: {pivote_seq(s6)} -> resposta = 3")
    print(f"teste 7: em {s7} a posição é: {pivote_seq(s7)} -> resposta = 2")
    print(f"teste 8: em {s8} a posição é: {pivote_seq(s8)} -> resposta = 5")
    print(f"teste 9: em {s9} a posição é: {pivote_seq(s9)} -> resposta = 0")
    print(f"teste 10: em {s10} a posição é: {pivote_seq(s10)} -> resposta = 3")

def pivote_seq(seq):

    # escreva sua solução
    '''
    primeiro, vou iniciar apresentando o pivo e as variáveis que vão procurar
    os máximos e os mínimos. O máximo vai percorrer da esquerda para a direita
    e o mínimo da direita para a esquerda
    '''
    pivo = len(seq) - 1
    maior = 0
    menor = pivo - 1
    
    # vou percorrer a lista até que o maior esteja a direita do menor
    while menor > 0 and maior < menor:
        if seq[menor] > seq[pivo]:
            menor -= 1
        elif seq[maior] < seq[pivo]:
            maior += 1
        else:
            if seq[menor] < seq[pivo]:
                if menor == len(seq) - 2:
                    seq=[seq[menor]]+seq[:menor]+[seq[pivo]]
                else:
                    seq=[seq[menor]]+seq[:menor]+seq[menor+1:pivo+1]
                # preciso atualizar maior
                # menor -= 1
            elif seq[maior] > seq[pivo]:
                #preciso verificar se já tem algum valor à esquerda do maior
                if maior == 0:
                    seq = seq[1:pivo] + [seq[maior],seq[pivo]]
                else:
                    seq = seq[:maior]+seq[maior+1:pivo] + [seq[maior],seq[pivo]]
      
    if  menor > 0 and seq[pivo] > seq[menor]:
        pivo = (menor+1)
    else:
        pivo = 0
    return pivo


#-----------------------------------------------        
if __name__ == '__main__':
    main()

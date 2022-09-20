'''
    Classe para o algoritmo de pilha.
'''


## ==================================================================
## Escreva a sua função palindromo()

def palindromo( s ):
    ''' 
    (String) --> Booleano
    A função recebe uma string e avalia se ela tem a mesma sequência se
    escrita na ordem inversa
    Exemplo:
        arara --> arara == True
        oito -- otio == False 
    
    Para isso colocar os itens da string (da esquerda para a direita) em uma 
    pilha e vou comparar se o topo dessa pilha é igual ao primeiro elemento da
    string e se os próximos elementos também são iguais
    '''
    pil = Pilha() # uso uma pilha vazia para a inversão
    # armazeno de trás para frente
    for i in s:
        pil.empilhe(i)
    # comparando os elementos:
    for j in range(len(s)):
        if s[j] != pil.topo():
            return False
        pil.desempilhe()
    return True
## ==================================================================
## Função de testes
def main():
    '''
    Função que executará testes para avaliar se o comportamento da classe Pilha
    é como o esperado
    '''
    

    pil = Pilha()   ## cria uma Pilha vazia
    print(f"pil.dados = {pil.dados}  --> deve ser a lista vazia []")
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser True")
    pil.empilhe('todos')
    pil.empilhe(4)
    pil.empilhe('paz')
    # Pilha.topo() apenas pega o valor no topo mas sem desempilher
    print(f"pil.topo() = {pil.topo()}  --> deve ser 'paz'") 
    pil.empilhe(True)
    print(f"len(pil) = {len(pil)} --> deve ser 4")  ## implemente o método __len__
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser False")
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz', True]")
    pil.empilhe(2.7)
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser 2.7")
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser True")
    print(f"len(pil) = {len(pil)} --> deve ser 3") 
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz']")
    
    #-----------------------------------------------------------------
    # Teste de palindromos 
    p1 = "arara"
    p2 = "este"
    p3 = "mirim"
    p4 = "radar"
    p5 = "rodo"
    
    print(f"{p1} é palíndromo: {palindromo(p1)} --> deve ser True ")
    print(f"{p2} é palíndromo: {palindromo(p2)} --> deve ser False ")
    print(f"{p3} é palíndromo: {palindromo(p3)} --> deve ser True ")
    print(f"{p4} é palíndromo: {palindromo(p4)} --> deve ser True ")
    print(f"{p5} é palíndromo: {palindromo(p5)} --> deve ser False ")
    
    #-------------------------------------------------------------
    # testes bem formada 
    print(f"bem_formada('(')--> {bem_formada('(')}")
    print(f"bem_formada(')(')-->{bem_formada(')(')}")
    print(f"bem_formada('(()))(')--> {bem_formada('(()))(')}")
    print(f"bem_formada('()()')--> {bem_formada('()()')}")
    print(f"bem_formada('(())')--> {bem_formada('(())')}")

## ============================================
def bem_formada( s ):
    ''' (str) -> bool
    recebe uma string s contendo uma sequência de abre e fecha parênteses
    e retorna True caso a sequência esteja bem formada e False caso contrário.

    Exemplos:
    >>> bem_formada('(')
    False
    >>> bem_formada(')(')
    False
    >>> bem_formada('(()))(')
    False
    >>> bem_formada('()()')
    True
    >>> bem_formada('(())')
    True
    '''
    
    pilha= Pilha()
    i=0
    while i<len(s):
        if s[i] == '(':
            pilha.empilhe(s[i])
        else:
            if pilha.vazia():
                return False
            else:
                pilha.desempilhe()
                
        i+=1 
    return pilha.vazia()
## ===================================================================
##
class Pilha:

    def __init__(self):
        '''
        Chamado pelo construtor da classe.
        Recebe uma referência 'self' ao objeto será uma lista usada para 
        formar a pilha        
        
        '''
        self.dados = []
        
    def __str__(self):
        '''
        Recebe uma referência self a um objeto da classe Pilha e cria e
        retorna a string que representa esse objeto

        '''
        return f"{self.dados}"
        
    def vazia(self):
        '''
        Avalia se a pilha está vazia e retorna uma variável booleana
        
        '''
        return self.dados == []
    
    def empilhe(self, item):
        '''
        Recebe um objeto que será colocado no topo da pilha
        '''
        return self.dados.append(item)
    
    def desempilhe(self):
        '''
        Remove o item no topo da pilha       
        '''
        return self.dados.pop()
    
    def topo(self):
        '''
        Retorna o item que está no topo da pilha        
        '''
        return self.dados[len(self.dados)-1]
    
    def __len__(self):
        '''
        Retorna o números de itens presentes na pilha
        '''
        return len(self.dados)

## ==================================================================
## Escreva outras funções e classes caso desejar


## ==================================================================
if __name__ == '__main__':
    main()
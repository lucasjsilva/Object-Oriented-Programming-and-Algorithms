'''
    (Array2d, tuple, obj) -> None
    Constrói um objeto do tipo Array2d com os atributos:
    data : lista onde os valores são armazenados
    shape: tupla que armazena as dimensões da matriz
    size : número total de elementos da matriz 
'''

## ==================================================================

def main():
    
    print("Testes da classe Array2d\n")
    
    # TESTES 3
    print("Testes da classe Array2d e comparação com Numpy\n")

    lista_a = [1, 2, 3, 4, 5, 6]
    lista_b = [0, 1, 1, 0, 0, 1]
    tam_a = len(lista_a)
    tam_b = len(lista_b)

    a = Array2d( (1, tam_a), 0) # cria Array2d com valor inicial 0
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print()
    a.data = lista_a   ## ou a.carregue(lista_a) como no EG10
    a.reshape( (2,3) )
    print(f'a:\n{a}\n')

    b = Array2d( (1, tam_b), 0)
    b.data = lista_b   # ou b.carregue(lista_b)
    b.reshape( (3,2) )
    print(f'b:\n{b}\n')

    linha = a.getlin(0)
    print(f'linha a.getlin(0)\n{linha}\n')

    coluna = b.getcol(1)
    print(f'coluna b.getcol(1)\n{coluna}\n')

    print(f'linha.dot(coluna)\n{linha.dot(coluna)}\n')

    print(f'matmul(a,b)\n{matmul(a,b)}\n')

    ### agora com Numpy
    import numpy as np
    npa = np.array( lista_a ).reshape((2,3))
    print(f'npa:\n{npa}\n')

    npb = np.array( lista_b ).reshape((3,2))
    print(f'npb:\n{npb}\n')

    print(f'np.matmul(npa, npb):\n{np.matmul(npa, npb)}\n')
    print('ao invés de np.matmul podemos usar @:')
    print(f'npa @ npb:\n{npa @ npb}\n')
    
    '''
    # TESTES 2
    # beginfora
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print()

    b = a.reshape( (2,3) )   
    print(f'teste 2: reshape cria uma vista')
    print(b)
    print()
    
    print(f'teste 3: mudanças em b devem resultar em mudanças em a:')
    b[1, 2] = 100
    print(a)
    print(b)
    print()

    print(f'teste 4: e vice-versa - mudanças em a devem resultar em mudanças em b:')
    a[0, 2] = -1 
    print(a)
    print(b)
    print()

    print(f'teste 5: copy cria um clone')
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    c = a.copy()
    print(f'a: {a}')
    print(f'c: {c}')
    print()

    print(f'teste 6: mudanças em objeto um não devem refletir no outro')
    a[0,1] = 99
    c[0,5] = -1
    print(f'a: {a}')
    print(f'c: {c}')
    print()
    
    lista = [1,2,3,4,5,6]
    a = Array2d( (2,3), 0)
    print(f'a:\n{a}\n')

    a.carregue( lista )
    print(f'a:\n{a}\n')
    
    a[1,1] = -1
    print(f'a:\n{a}\n')
    print(f'lista: {lista}')
    
    lista = [1,2,3,4,5,6]
    a = Array2d( (2,3), 0)
    print(f'a:\n{a}\n')

    a.carregue2( lista )
    print(f'a:\n{a}\n')

    a[1,1] = -1
    print(f'a:\n{a}\n')
    print(f'lista: {lista}')
    
    lista = [1,2,3,4,5,6,7,8,9,0]
    a = Array2d( (5,2), 0)
    a.carregue( lista )
    print(f'a:\n{a}\n')
    
    flip = a.flipV()
    print(f'flip:\n{flip}\n')
    
    print(f'a:\n{a}\n')
    '''

    '''
    #TESTES 1
    print("Testes da classe Array2d\n")
    a = Array2d( (2,3), 3) # cria Array2d com valor inicial 3
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print(f'shape: {a.shape}')
    print(f'size : {a.size}')
    print(f'data : {a.data}')
    print()

    b = Array2d( (2,3), 1.7)   # criar Array2d com valor inicial 7
    print(f'teste 2: Criação do Array2d b:')
    print(b)
    print(f'shape: {b.shape}')
    print(f'size : {b.size}')
    print(f'data : {b.data}')
    print()

    print(f'teste 3: a[0,1] + 100 é: {a[0,1] + 100}') # acesso direto usando tupla: use o método __getitem__
    print()

    a[1,1] = -1    # atribuição usando tupla: use o método __setitem__
    print(f'teste 4: Array2d a:')
    print(a)
    
    a[0,2] = 12 # atribuição
    print(f'teste 5: Array2d a:')
    print(a)
    
    c = Array2d( (5,5), True)   # criar Array2d com valor inicial 7
    print(f'teste 2: Criação do Array2d c:')
    print(c)
    print(f'shape: {c.shape}')
    print(f'size : {c.size}')
    print(f'data : {c.data}')
    print()
    '''

# ===================================================================
def matmul(array1, array2):
    
    '''
    (Array2d e Array2d) -> Array2d
    Duas Arrays de dimensões diferentes são multiplicadas
    entre si retornando o produto matricial entre elas
    '''
    lin_s, col_s = array1.shape
    lin_o, col_o  = array2.shape
    dados_s = array1.data
    dados_o = array2.data
    produto = []
    if lin_s == col_o:
        for i in range(lin_s):
            valores = 0
            for j in range(col_o):
                valores = 0
                for k in range(lin_o):
                    valores += dados_s[((i*col_s)+k)]*dados_o[((col_o*k)+j)]
                produto.append(valores)
        array = Array2d((lin_o,col_s), produto) 
        
    if lin_o == col_s:
        for i in range(lin_o):
            for j in range(col_s):
                for k in range(lin_s):
                    valores +=dados_o[((i*col_o)+k)]*dados_s[((col_s*k)+j)]
                produto.append(valores)
        array =Array2d((lin_s,col_o), produto)
    else:
        return None
    
    return array

## ==================================================================
#   A classe Array2d permite a manipulação de 'matrizes' de duas 
#   dimensões. O exercício é utilizar uma lista linear, ao invés
#   de uma lista aninhada, para armazenar os dados da matriz 
#   internamente.
#   A lista linear deve ser um atributo de nome 'data'.

class Array2d:

    # ---------------------------------------------------------------
    def __init__(self, shape, val):
        self.shape = shape
        self.size = shape[0]*shape[1]
        if type(val) == list:
            self.data = val
        else:
            self.data = [val]*self.size

    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (Array2d, tupla) -> obj
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do Array2d self.

        Esse método é usado quando o objeto é chamado com 
        uma tupla entre colchetes, como self[0,0]. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> a[1,1] + 100
        99
        >>> print( a[1,1] )
        -1
        '''
        lista = self.data 
        dim = self.shape # dimensão da matriz
        # fórmula para encontrar o elemento:
        # (linha - 1) * n_linhas da matriz + coluna 
        elem = key[0]*dim[1] + key[1]
        
        return lista[elem]

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (Array2d, tupla, obj) -> None
        recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do Array2d self.

        Esse método é usado para atribuir 'valor' na posição
        indicada pela tupla `key`, como self[0,0] = 0. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> print( a[1,1] )
        -1
        >>> a[1,1] = 100
        >>> print( a[1,1] )
        100
        '''
        lista = self.data 
        dim = self.shape # dimensão da matriz
        elem = (key[0])*dim[1] + key[1]
        
        lista[elem] = valor

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Array2d) -> None
        ao ser usada pela função print, deve exibir cada linha
        do Array2d em uma linha separada, separando seus elementos por um espaço.

        Exemplo: para self.data = [1, 2, 3, 4, 5, 6] e self.shape = (2,3)
        o método deve retornar a string 
        "1 2 3\n4 5 6" 
        e, caso self.shape = (3,2) o método deve retornar a string
        "1 2\n3 4\n5 6" 
        '''
        lin = self.shape[0]
        col = self.shape[1]
        valores = self.data
        # printar fatia
        # palavra = str
        x = " "
        for i in range(lin):
            for j in range(i*col, (i+1)*col):
                if x == " ":
                    x = str(valores[j]) + " "
                else:
                    x += str(valores[j]) + " "
            x += "\n"
        return x
    # --------------------------------------------------------------
    def copy(self):
        '''
        (Array2d) -> obj
        ao ser usada a função copy retorna uma cópia completa do objeto do tipo
        Array2d, incluindo uma cópia do item data
        '''
        copia = Array2d(self.shape, self.data[:])
        return copia

    # ---------------------------------------------------------------
    def reshape(self, key):
        '''
        (Array2d) -> None
        Recebe uma tupla key com uma dimensão (nlin,ncol) e retorna uma vista do
        objeto Array2d com uma nova dimensão
        '''
        self.shape=key
        #return(Array2d(key, self.data))
    
    # ---------------------------------------------------------------
    def carregue2(self,key):
        ''' 
        '''
        self.data=key[:]
        
    # ----------------------------------------------------------------
    def getlin(self, lin):
        '''
        (Array2d) -> Array2d
        Recebe um inteiro e devolve a linha da array
        '''
        col = self.shape[1] 
        dados = self.data
        linha = dados[lin*col:(lin+1)*col]
        
        return (Array2d((1,col), linha))
    
    # -----------------------------------------------------------------        
    def getcol(self,col):
        '''
        (Array2d) -> Array2d
        Recebe um inteiro e devolve a linha da array
        '''
        lin,cols = self.shape
        dados = self.data
        coluna = dados[col:(lin*cols)-(cols-(col+1)):cols]
        
        return (Array2d((lin,1), coluna))
        
    # ------------------------------------------------------------------
    def dot(self,other):
        '''
        (Array2d e Array2d) -> escalar
        Duas arrays com o mesmo número de elementos são 
        multiplicadas termo a termo resultando em um escalar
        '''
        tam = self.size
        produto = 0
        dados_s = self.data # dados do self
        dados_o = other.data # dados do other
        for i in range(tam):
            produto+=dados_s[i]*dados_o[i]
        
        return(produto)
    
    # ------------------------------------------------------------------
    
## ==================================================================

if __name__ == '__main__':
    main()
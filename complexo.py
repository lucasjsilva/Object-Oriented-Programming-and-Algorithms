'''
    Classe para um n�mero complexo realizando opera��es de soma e multiplica��o    
'''
# ===================================================================
def main():
    '''
    O main ser� usado para testes da Classe Complexo

    '''
    complexo0 = Complexo( )
    complexo1 = Complexo(1,3)
    complexo2 = Complexo(2,4)
    complexo3 = Complexo(5,-2)
    complexo4 = Complexo(-1,-1)
    
    print("TESTE N�MEROS COMPLEXOS")
    print("Complexo()=",complexo0)
    print("Complexo(1,3)=", complexo1)
    print("Complexo(2,4)=", complexo2)
    print("Complexo(5,-2)=", complexo3)
    print("Complexo(-1,-1)=", complexo4)
    
    print("TESTE PARA A SOMA:")
    print(f"(1,3)+(2,4)={complexo1.some(complexo2)}")
    print(f"(0,0)+(2,4)={complexo0.some(complexo2)}")
    print(f"(0,0)+(1,3)={complexo0.some(complexo1)}")
    print(f"(1,3)+(5,-2)={complexo1.some(complexo3)}")
    print(f"(2,4)+(-1,-1)={complexo2.some(complexo4)}")
    
    print("TESTE PARA MULTIPLICA��O:")
    print(f"(1,3)*(2,4)={complexo1 * complexo2}")
    print(f"(0,0)*(1,3)={complexo0 * complexo1}")
    print(f"(5,-2)*(-1,-1)={complexo3*complexo4}")
    print(f"(1,3)*(-1,-1)={complexo1*complexo4}")
    
# ===================================================================

class Complexo:
    '''Classe utilizada para representar um número Complexo.

    Um complexo é representado por dois números reais. 
    Assim, cada objeto dessa classe terá dois atributos de estado:
 
       * `real`: um número real que corresponde à parte real
       * `imag`: um número real que corresponde à parte imaginária
 
    Você deverá escrever os métodos a seguir.
    '''

    #------------------------------------------------------------------------------
    def __init__(self, r = 0.0, i = 0.0):
        '''(Complexo, float, float) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os reais `r` e `i` que 
        representam o número complexo.

        Exemplos:

        >>> c0 = Complexo() # construtor chama __init__()
        >>> c0.real
        0.0
        >>> c0.imag
        0.0
        >>> c1 = Complexo(9)
        >>> print(c1.real, c1.imag)
        9.0 0.0
        >>> c2 = Complexo(9,4)
        >>> print(c2.real, c2.imag)
        9.0 4.0
        >>> 
        '''
        
        self.real = r
        self.imag = i
        
    #------------------------------------------------------------------------------        
    def __str__(self):
        '''(Complexo) -> str

        Recebe uma referencia `self` a um objeto da classe Complexo e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplos:

        >>> ini = Complexo(8)
        >>> fim = Complexo(9,4)
        >>> fim.__str__()
        '9.0+j4.0'
        >>> ini.__str__() # chamada do método __str__()
        '8.0'
        >>> str(ini) # função str() exibe a string criada por __str__()
        '8.0'
        >>> str(fim) 
        '9.0+j4.0'
        >>> print(fim) # exibe o string criado por __str__()
        9.0+j4.0
        >>> print(ini)
        8.0
        >>>         
        '''
        if self.imag >= 0:
            return f"{self.real}+j{self.imag}"
        else:
            return f"{self.real}-j{-self.imag}"

    #------------------------------------------------------------------------------        
    def some(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referência `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado da soma self + other
        
        Exemplos:

        >>> c0 = Complexo(8)
        >>> c1 = Complexo(9,4)
        >>> c2 = c0.some(c1)
        >>> print(c2)
        17.0+j4.0
        >>>         
        '''
        soma_real = self.real + other.real
        soma_imag = self.imag + other.imag
        return Complexo(soma_real, soma_imag)

    #------------------------------------------------------------------------------        
    def __mul__(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referência `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado do produto self * other
        
        Exemplos:

        >>> comp0 = Complexo(1, 2)
        >>> comp1 = Complexo(3, 4)
        >>> comp2 = comp0 * comp1
        >>> print(comp2)
        -5.0+j10.0
        >>>         
        '''
        mul_real = self.real*other.real - self.imag*other.imag
        mul_imag = self.real*other.imag + self.imag*other.real
        return Complexo(mul_real, mul_imag)
    
# ============================================================================
if __name__ == "__main__":
    main()

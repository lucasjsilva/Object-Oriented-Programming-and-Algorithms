'''
    Essa classe Fraction foi adaptada da seção 1.13.1 Uma Classe Fraction
    do capítulo 1 do livro Resolução de Problemas com Algoritmos e 
    Estruturas de Dados usando Python disponível no endereço
    https://panda.ime.usp.br/panda/static/pythonds_pt/index.html. 

    A classe Fraction representa uma fração. 
    Uma fração é constituída por um numerador e um denominador, 
    ambos inteiros, como por exemplo 2/5 (dois quintos), 
    onde 2 é o numerador e 5 o denominador
     
'''

# ===================================================================

def main():
    '''
        Programa main usado para teste da classe Fraction.
    '''

    # Criação de objetos do tipo Fraction 
    f12 = Fraction(1,2)
    f34 = Fraction(3,4)

    # soma 2 fracoes
    soma = f12 + f34
    print(f"{f12} + {f34}      = {soma}")
    print(f"Resultado esperado = 5/4 ")

    # soma fracao com inteiro
    soma = f12 + 2
    print(f"{f12} + 2         = {soma}")
    print(f"Resultado esperado = 5/2 ")

    # soma inteiro com fracao
    soma = 2 + f34
    print(f"  2 + {f34}      = {soma}")
    print(f"Resultado esperado = 11/4 ")

    # ===================================================================
    # Escreva outros testes
    
    f105 = Fraction(10, 5)
    f4020 = Fraction(40, 20)
    f74 = Fraction(7, 4)
    i2 = 2
    i3 = 3
    f279 = Fraction(27, 9)
    f21 = Fraction(2, 1)
    
    # divisão
    div = f105/2
    print(f"{f105}/{i2} = {div}")
    print(f"Resultado esperado é 1/1")
    
    div = f34/f105
    print(f"({f34})/({f105}) = {div}")
    print(f"Resultado esperado é 3/8")
    
    div = i3/f74
    print(f"({i3})/({f74}) = {div}")
    print(f"Resultado esperado é 12/7")
    
    div = f4020/f279
    print(f"({f4020})/({f279}) = {div}")
    print(f"Resultado esperado é 2/3")
    
    # igualdade 
    
    igualdade = i2 == f105
    print(f"{i2} é igual a {f105}: {igualdade}")
    print(f"Resultado esperado = True")
    
    igualdade = f279 == i3
    print(f"{f279} é igual a {i3}: {igualdade}")
    print(f"Resultado esperado = True")
    
    igualdade = f105 == f21
    print(f"{f105} é igual a {f21}: {igualdade}")
    print(f"Resultado esperado = True")
    
    igualdade = (f105 == f4020)
    print(f"{f105} é igual a {f4020}: {igualdade}")
    print(f"Resultado esperado = True")
    
    igualdade = f105 == f74
    print(f"{f105} é igual a {f74}: {igualdade}")
    print(f"Resultado esperado = False")
    
    igualdade = i3 == f105
    print(f"{i3} é igual a {f105}: {igualdade}")
    print(f"Resultado esperado = False")
    
    # maior e menor
    
    maior = (i3 >= f105)
    print(f"{i3} é maior ou igual que que {f105}: {maior}")
    print(f"Resultado esperado = True")
    
    maior = (f34 >= f279)
    print(f"{f34} é maior ou igual que que {f279}: {maior}")
    print(f"Resultado esperado = False")
    
    menor = (f105 <= f74)
    print(f"{f105} é menor ou igual que que {f74}: {menor}")
    print(f"Resultado esperado = False")
    
    menor = (f105 <= i3)
    print(f"{f105} é menor ou igual que que {i3}: {menor}")
    print(f"Resultado esperado = True")
    
    menor = (i2 <= f4020)
    print(f"{i2} é menor ou igual que que {f4020}: {menor}")
    print(f"Resultado esperado = True")
    
# ===================================================================
class Fraction:
    
    def __init__(self, cima, baixo):
        '''(Fraction, int, int) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os inteiros cima e baixo que representam
        a fração.

        Exemplos:

        >>> frac = Fraction(2,5) # construtor chama __init__()
        >>> frac.num
        2
        >>> frac.den
        5
        '''
        self.num = cima
        self.den = baixo

    def __str__(self):
        '''(Fraction) -> str

        Recebe uma referencia `self` a um objeto da classe Fraction e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplo:

        >>> frac = Fraction(2,5)
        >>> print(frac)
        2/5
        '''
        return f"{self.num}/{self.den}"
    
    def meu_mdc( self, a, b ):
        ''' (Fraction, int, int) -> int 
        recebe dois inteiros a e b, e 
        retorna o mdc entre a e b.
        '''
        aa = abs(a)
        ab = abs(b)
        mdc = min(aa, ab)
        if mdc == 0: return max(aa, ab)
        while (aa % mdc != 0) or (ab % mdc != 0): 
            mdc -= 1
        return mdc
    
    #------------------------------------
    def __add__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a soma da Fraction `self` e da Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction + Fraction ou
                                            Fraction + int
        """
        if type(other) is int:
            cima = self.num + other*self.den
            baixo = self.den
        else:
            cima = self.num*other.den + other.num*self.den
            baixo = self.den*other.den
            
        comum = self.meu_mdc(cima, baixo) # simplifica a fração
            
        return Fraction(cima//comum, baixo//comum)

    #------------------------------------
    def __radd__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a soma da Fraction `self` e int `other`.
        Usado pelo Python quando escrevemos int + Fraction
        """
        cima = self.den*other + self.num
        baixo = self.den
        comum = self.meu_mdc(cima, baixo) # simplifica a fração
        return Fraction(cima//comum, baixo//comum)
        
    #-------------------------------------
    def __truediv__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a divisão da Fraction `self` pela Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction / Fraction ou
                                            Fraction / int
        """
        # caso seja Fraction/int:
        if type(other) is int:
            cima = self.num
            baixo = self.den*other
        # caso seja Fraction/Fraction
        else:
            cima = self.num*other.den
            baixo = self.den*other.num
        
        comum = self.meu_mdc(cima, baixo) # simplifica a fração
        
        return Fraction(cima//comum, baixo//comum)

    #-------------------------------------
    def __rtruediv__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a divisão do int `other` pela Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """
        cima = self.den*other
        baixo = self.num
        comum = self.meu_mdc(cima, baixo) # simplifica a fração
        
        return Fraction(cima//comum, baixo//comum)

    #-------------------------------------
    def __eq__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a comparação da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction == Fraction ou
                                            Fraction == int
        """
        cima1 = self.num
        baixo1 = self.den
        comum_s = self.meu_mdc(cima1, baixo1)
        # Caso do int
        if type(other) is int:
            if baixo1 == 1 and cima1 == other or (baixo1//comum_s == 1 and cima1//comum_s == other):
                return True
            else:
                return False
        else:
            cima2 = other.num
            baixo2 = other.den
            comum_o = self.meu_mdc(cima2, baixo2)
            if (baixo1 == baixo2 and cima1 == cima2) or (baixo1//comum_s==baixo2//comum_o and cima1//comum_s == cima2//comum_o):
                return True
            else:
                return False 

    #-------------------------------------
    def __req__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a comparação do int `other` com a Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """
        cima = self.num
        baixo = self.den
        comum = self.meu_mdc(cima, baixo)
        if (baixo == 1 and cima == other) or (baixo//comum == 1 and cima//comum == other):
            return True
        else:
            return False
        
    #-----------------------------------
    def __gt__(self, other):
        """ (Fraction, Fraction ou int) -> bool

        Retorna a comparação da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction > Fraction ou
                                            Fraction > int
        """
        cima_s = self.num
        baixo_s = self.den
        comum_s = self.meu_mdc(cima_s, baixo_s)
        
        if type(other) is int:
            if (baixo_s//comum_s == 1 and cima_s//comum_s >= other):
                return True
            else:
                return False
        else:
            cima_o = other.num
            baixo_o = other.num
            comum_o = self.meu_mdc(cima_o, baixo_o)    
            # para comparar preciso analisar os numeradores
            if ((cima_s//comum_s)*(baixo_o//comum_o) >= (cima_o//comum_o)*(baixo_s//comum_s)):
                return True
            else:
                return False
            
    #-----------------------------------
    def __rgt__(self, other):
        """ (Fraction, int) -> bool

        Retorna a comparação do int `other` com a Fraction `self`.
        Usado pelo Python quando escrevemos int > Fraction
        """
        return self >= other

    #-------------------------------------
    def __le__(self, other):
        """ (Fraction, Fraction ou int) -> bool

        Retorna a comparação da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction <= Fraction ou
                                            Fraction <= int
        """
        
        cima_s = self.num
        baixo_s = self.den
        comum_s = self.meu_mdc(cima_s, baixo_s)
        
        if type(other) is int:
            if (baixo_s//comum_s == 1 and cima_s//comum_s <= other):
                return True
            else:
                return False
        else:
            cima_o = other.num
            baixo_o = other.num
            comum_o = self.meu_mdc(cima_o, baixo_o)    
            # para comparar preciso analisar os numeradores
            if ((cima_s//comum_s)*(baixo_o//comum_o) <= (cima_o//comum_o)*(baixo_s//comum_s)):
                return True
            else:
                return False

    #-------------------------------------
    def __ge__(self, other):
        """ (Fraction, int) -> bool

        Retorna a comparação do int `other` com a Fraction `self`.
        Usado pelo Python quando escrevemos int <= Fraction
        """
        return self <= other

## =============================================================
#  fim da definição de todas as funções e classes
#  chama a main
## =============================================================
if __name__ == "__main__":
    main()
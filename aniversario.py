import random

## ==================================================================
#     Constantes que você pode usar em sua solução

DATAS = 365
SUCESSO = True
FRACASSO = False

## ==================================================================
# 
def main():
    '''
    Testes da classe Aniversario

    inclua mais 10 testes usando valores distintos de n e t.
    '''

    print("Testes do EI27 - Paradoxo do Aniversário")
    
    pessoas = [5, 5, 10,
              10, 30, 30,
              50, 50, 100, 100]
    
    tentativas = [5, 100, 5,
                  100, 10, 100,
                  10, 100, 10, 100]
    
    for i in range(len(tentativas)):
        print(f"Com {pessoas[i]} pessoas e {tentativas[i]} tentativas obtevesse {Aniversario(pessoas[i], tentativas[i])}")

## ==================================================================
# 
class Aniversario:

    #------------------------------------------
    def __init__(self, n, t):
        '''(Aniversario, int, int) -> None

        Recebe o número n de pessoas que podem entrar na sala
        e o número t de experimentos (trials). 
        Calcula a probabilidade de, ao selecionarmos n 
        datas uniformemente ao acaso, tenhamos
        duas datas iguais.
        '''        
        self.n = n
        self.t = t
        sucessos = 0
        for i in range(t):
            sucessos += self.experimento()
        self.p = sucessos/t    

    #------------------------------------------    
    def __str__(self):
        return str(self.p)

    #------------------------------------------    
    def mean(self):
        return self.p

    #-----------------------------------------
    def experimento(self):
        ''' (Aniversario) -> bool

        Executa um experimento como descrito no enunciado,
        para uma sala com até 
        * self.n pessoas e 
        * self.t tentativas (trials)
        Retorna SUCESSO ou FRACASSO.

        DICA: para esse método, conjuntos são mais 
        eficientes que listas.
        '''
        # primeiro vou atribuir algumas variáveis
        n = self.n # número de pessoas
        conj = set() # vai armazenar todos os valores
        
        # para cada pessoa que entra na sal eu sorteio um núm aleatório
        for i in range(n):
            # sorteio o número e então avalio se está no conjunto
            aleatorio = random.randrange(0, 365, 1) 
            if aleatorio in conj:
                return True
            else:
                conj.add(aleatorio)
            
        # caso percorra tudo e não encontre, a função deve retornar false
        return False
            
        

        # implemente sua solução

## ==================================================================
# 
if __name__ == '__main__':
    main()
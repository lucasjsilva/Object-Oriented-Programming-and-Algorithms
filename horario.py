'''
    Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.
 
      * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
      * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
      * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos 
'''

#================================================================

def main():
    print("Executando a main() no arquivo horario.py")

    print("Teste da classe Horario")
    t0 = Horario()      
    print("t0 = ", t0)

    print(f"__name__ dentro do arquivo horario.py = {__name__}")
    print("Fim da main() no arquivo horario.py")


def main_velha():

    t1 = Horario(8,0,0)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = Horario(1,40)
    print(f't2 = {t2} e deve ser 01:40:00')

    t3 = t1 + t2
    print(f't3 = {t3} e deve ser 09:40:00')

    t4 = t1 + Horario(0,100)  ## 100 minutos equivale a 01:40
    print(f't4 = {t4} e deve ser 09:40:00') 

    print(f't4 == t3 é {t4 == t3} e deve ser True')
    print(f't1 >  t2 é {t1 >  t2} e deve ser True')
    print(f't1 >= t2 é {t1 >= t2} e deve ser True')
    print(f't1 <  t2 é {t1 <  t2} e deve ser False')
    print(f't1 <= t2 é {t1 <  t2} e deve ser False')
    print(f't1 == t2 é {t1 == t2} e deve ser False')

    t5 = Horario(23,59,59)
    t6 = Horario(0,0,1)
    t7 = t5 + t6
    print(f't7 = {t7} e deve ser 00:00:00')

    t8 = t1 - t2  
    print(f't8 = {t8} e deve ser 06:20:00')

    t9 = t2 - t1   ##   nao temos horarios negativos
    print(f't9 = {t9} e deve ser 00:00:00')

    print(f't2.dados = {t2.dados} e deve ser a lista [0, 40, 1]')
    
    t10 = Horario(3,41,50)
    t11 = Horario(0,50,52)
    t12 = t10 - t11
    print(f't12 = {t12} e deve ser 02:50:58')

# ===============================================================
class Horario:
    
    def __init__(self, horas = 0, minutos = 0, segundos = 0 ):
        '''
        Chamado pelo construtor da classe.
        Recebe uma referência 'self' ao objeto será uma lista guardado os
        valores de segundos, minutos e horas, respectivamente.
        
        Exemplo:
            >>> tempo=Horario(2,5,7)
            >>>tempo.hora
            2
            >>>tempo.minut
            5            
            >>>tempo.seg
            7
        '''
        data = [segundos, minutos, horas]
        for i in range(len(data)):
            if i == 2:
                if data[i] > 23:
                    data[i] -= 24 # garante que o limite das horas vá de 0 a 23
            else:
                if data[i] > 59:
                    # se seg o min for >= 60 preciso acrescentar na hora ou no min
                    data[i+1] += data[i]//60 
                    # garantir que o limite dos min e seg vá de 0 a 59
                    data[i] -= (data[i]//60)*60 
                    
        self.dados = data
        
    def __str__(self):
        '''
        (Horario) --> str
        Recebe uma referência self a um objeto da classe Horario e cria e
        retorna a string que representa esse objeto
        
         Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplo:
        >>> tempo=Horario(2,5,7)
        >>> print (tempo)
        02:05:07
        '''
        sec = self.dados[0]
        minute = self.dados[1]
        hour = self.dados[2]
        if sec < 10:
            sec = f"0{sec}"
        if minute < 10:
            minute = f"0{minute}"
        if hour < 10:
            hour = f"0{hour}"
        
        return f"{hour}:{minute}:{sec}"
    
    def __add__(self, other):
        '''
        (Horario) --> Horario
        Retorna a soma de dois horários, um self mais um other
        No python escrevemos como Horario + Horario        
        '''
        segundos = self.dados[0] + other.dados[0]
        minutos = self.dados[1] + other.dados[1]
        horas = self.dados[2] + other.dados[2]
        return Horario(horas, minutos, segundos)
        
    def __sub__(self, other):
        '''
        (Horario) --> Horario
        Retorna a subtração de dois horários, um self mais um other
        No python escrevemos como Horario + Horario        
        '''
        segundos = self.dados[0] - other.dados[0]
        minutos = self.dados[1] - other.dados[1]
        horas = self.dados[2] - other.dados[2]
        
        # caso sejam negativos
        if segundos < 0:
            segundos = (60+self.dados[0]) - other.dados[0]
            minutos -= 1
            if minutos < 0:
                # tenho que subtrair um dos minutos que foi emprestado pros segundos
                minutos = (60 + self.dados[1]-1) - other.dados[1]
                horas = (self.dados[2]-1)-other.dados[2]
        if minutos < 0:
            minutos = (60 + self.dados[1]) - other.dados[1]
            horas = (self.dados[2]-1)-other.dados[2]
        elif horas < 0:
            return Horario()
                    
        return Horario(horas, minutos, segundos)
        
    def __eq__(self, other):
        '''
        (Horario) --> Horario
        Retorna a comparação de que se dois horários são iguais.
        Em Python escrevemos Horario == Horario

        '''
        segundos_s = self.dados[0]
        segundos_o = other.dados[0]
        minutos_s = self.dados[1]
        minutos_o = other.dados[1]
        horas_s = self.dados[2]
        horas_o = other.dados[2]
        
        if (minutos_s == minutos_o) and (segundos_o == segundos_s) and (horas_o == horas_s):
            return True
        else:
            return False
        
    def __gt__(self, other):
        '''
        (Horario) -->
        Retorna a comparação se o horário 'self' é maior que o horário 'other'
        Em python escrevemos Horario > Horario
        '''
        segundos_s = self.dados[0]
        segundos_o = other.dados[0]
        minutos_s = self.dados[1]
        minutos_o = other.dados[1]
        horas_s = self.dados[2]
        horas_o = other.dados[2]
        
        if horas_s > horas_o:
            return True
        if horas_s == horas_o:
            # preciso analisar os minuto e então os segundos
            if minutos_s > minutos_o:
                return True
            if minutos_s < minutos_o:
                return False
            else:
                if segundos_s > segundos_o:
                    return True
                else:
                    return False
        else:
            return False
        
    def __lt__(self, other):
        '''
        (Horario) --> Horario
        Retorna a comparação se o horário 'self' é menor que o horário 'other'
        Em python escrevemos Horario < Horario
        '''
        segundos_s = self.dados[0]
        segundos_o = other.dados[0]
        minutos_s = self.dados[1]
        minutos_o = other.dados[1]
        horas_s = self.dados[2]
        horas_o = other.dados[2]
        
        if horas_s < horas_o:
            return True
        if horas_s == horas_o:
            # preciso analisar os minuto e então os segundos
            if minutos_s < minutos_o:
                return True
            if minutos_s > minutos_o:
                return False
            else:
                if segundos_s < segundos_o:
                    return True
                else:
                    return False
        else:
            return False
        
    def __ge__(self, other):
        '''
        (Horario) --> Horario
        Retorna a comparação se o horário 'self' é maior ou igual que o 
        horário 'other' 
        Em python escrevemos Horario >= Horario
        '''
        if self.__eq__(other) == False:
            return self.__gt__(other)
        else:
            return True
    
    def __le__(self, other):
        '''
        (Horario) --> Horario
        Retorna a comparação se o horário 'self' é menor  ou igual que o 
        horário 'other'
        Em python escrevemos Horario <= Horario
        '''
        if self.__eq__(other) == False:
            return self.__lt__(other)
        else:
            return True
        
# ===============================================================
#if __name__ == '__main__':
main()
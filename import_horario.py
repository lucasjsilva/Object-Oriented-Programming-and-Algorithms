## usando um apelido para o módulo Horario
from horario import main
import horario as hor

def main():
    print("Executando a main() no arquivo programa.py")
    print(f"__name__ dentro do arquivo programa.py = {__name__}")

    t1 = hor.Horario(8,0,0)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = hor.Horario(1,40)
    print(f't2 = {t2} e deve ser 01:40:00')

    t3 = t1 + t2
    print(f't3 = {t3} e deve ser 09:40:00')

    t4 = t1 + hor.Horario(0,100)  ## 100 minutos equivale a 01:40
    print(f't4 = {t4} e deve ser 09:40:00') 

    print(f't4 == t3 é {t4 == t3} e deve ser True')
    print(f't1 >  t2 é {t1 >  t2} e deve ser True')
    print(f't1 >= t2 é {t1 >= t2} e deve ser True')
    print(f't1 <  t2 é {t1 <  t2} e deve ser False')
    print(f't1 <= t2 é {t1 <  t2} e deve ser False')
    print(f't1 == t2 é {t1 == t2} e deve ser False')

    t5 = hor.Horario(23,59,59)
    t6 = hor.Horario(0,0,1)
    t7 = t5 + t6
    print(f't7 = {t7} e deve ser 00:00:00')

    t8 = t1 - t2  
    print(f't8 = {t8} e deve ser 06:20:00')

    t9 = t2 - t1   ##   nao temos horarios negativos
    print(f't9 = {t9} e deve ser 00:00:00')

    print(f't2.dados = {t2.dados} e deve ser a lista [0, 40, 1]')

    # inclua outros testes caso desejar

if __name__ == '__main__':
    main()
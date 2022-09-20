# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''
    (str) -> bool
    Recebe uma string seq contendo uma sequência formada pelos
    caracteres '()[]{}'. 
    Retorna True caso a sequência esteja bem formada e False em
    caso contrário.
    A função deve ignorar caracteres diferentes de '()[]{}' 
    sem resultar em erro.
    Exemplos:
    >>> bem_formada( "(a+ {b })-{2*[3+4]}" )
    True
    >>> bem_formada( "( ( (  ) " )
    False
    >>> bem_formada( " { ( { x } )  } [ y ]" )
    True
    >>> bem_formada( " { ( { x }  } [ y ] )" )
    False 
'''

ABRE = '([{'
FECHA = ')]}'

def main():
    ''' função para teste da função bem_formada
    '''
    teste0 = "()"
    teste1 = "(([]))"
    teste2 = "{)}"
    teste3 = "{[][]([])}()"
    teste4 = "[(){}(]"
    teste5 = "}}()()[]"
    teste_a = "{y*[2+x][-4](1-[3+y])**3}/(x-y)"
    print(f"{teste0} é balanceada --> {bem_formada(teste0)} e a resposta é True")
    print(f"{teste1} é balanceada --> {bem_formada(teste1)} e a resposta é True")
    print(f"{teste2} é balanceada --> {bem_formada(teste2)} e a resposta é False")
    print(f"{teste3} é balanceada --> {bem_formada(teste3)} e a resposta é True")
    print(f"{teste4} é balanceada --> {bem_formada(teste4)} e a resposta é False")
    print(f"{teste5} é balanceada --> {bem_formada(teste5)} e a resposta é False")
    print(f"{teste_a} é balanceada --> {bem_formada(teste_a)} e a resposta é True")

# ---------------------------------------------------------

def bem_formada( seq ):
    
    lista = [] # lista que vai receber as variáveis
    for i in seq:
        if i == "(" or i == "[" or i == "{":
            lista.append(i)
        if len(lista) != 0:
            if i == ")":
                if lista[-1] == "(":
                    # Pode desempilhar
                    lista.pop()
                else:
                    return False
            if i == "]":
                if lista[-1] == "[":
                    # Pode desempilhar
                    lista.pop()
                else:
                    return False
            if i == "}":
                if lista[-1] == "{":
                    # Pode desempilhar
                    lista.pop()
                else:
                    return False
            if i == "$":
                if lista[-1] == "$":
                    # Pode desempilhar
                    lista.pop()
                else:
                    return False
        else:
            if len(lista) == 0 and i == ")" or i == "]" or i == "}":
                return False
            
    if len(lista) == 0: 
        return True
    else:
        return False

# ---------------------------------------------------------

if __name__ == '__main__':
    main()
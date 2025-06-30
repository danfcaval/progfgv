




def pares_e_impares(nums: list[int]):
    """ Recebe uma lista de inteiros e retorna uma tuple com (pares, impares) """

    impares = [] #output impares
    pares = [] #output pares

    for num in nums: #iterando input

        if type(num) is not int: #teste basico de tipo
            continue

        if num % 2 == 0: #se a sobra da divisao por 2 for 0, eh par
            if(num not in pares):
                pares.append(num)
        else:
            if(num not in impares):
                impares.append(num)

    return (pares, impares)


def filtrar_por_tamanho(lista: list[str], k: int):
    """ Recebe uma lista de strings e um inteiro, e retorna palavras > o inteiro """

    resposta = [] #output

    for palavra in lista:
        if type(palavra) is not str: #teste basico de tipo
            continue

        if len(palavra) > k : #testa tamanho da string para adicionar ao output
            resposta.append(palavra)
    
    return resposta


def rotate_tuple(tpl: tuple, n: int):
    """ Recebe uma tuple e um inteiro (n), e retorna uma tuple rotacionada n posicoes para direita """

    tamanho_tpl = len(tpl) #tamanho total da tuple
    vezes_n_maior_tpl = n // tamanho_tpl #multiplicador que sera utilizado para saber quantas vezes o inteiro vai nos fazer percorrer a tuple por completa
    subtrator = tamanho_tpl * vezes_n_maior_tpl #subtrator para remover da posicao final as vezes totais que vamos percorrer a tuple

    resposta = [None] * tamanho_tpl #output to mesmo tamanho da tuple

    for indice, valor in enumerate(tpl): #usado enumerate para ter valores da tuple e sua posicao
        posicao_desejada = indice + n - subtrator #nova posicao calculada como posicao atual + inteiro - subtrator de vezes percorrido por completo

        if posicao_desejada >= tamanho_tpl: #se nao percorreu uma vez por completo mas mesmo assim ficou como depois do fim da tuple
            posicao_desejada = posicao_desejada - tamanho_tpl #subtrai uma vez o tamanho da tuple

        resposta[posicao_desejada] = valor

    return tuple(resposta)

def transpose(matrix: list[list]):
    """ Recebe uma matriz como uma lista de lists e retorna a transposta """

    rows = len(matrix) #numero de linhas
    cols = len(matrix[0]) #numero de colunas
    resposta = [] #output

    for col_num in range(cols): #iterando as posicoes da coluna
        new_row = []

        for row_num in range(rows): #iterando as posicoes das linhas
            new_row.append(matrix[row_num][col_num]) #criando nova linha com valores de cada coluna

        resposta.append(new_row) #adicionando nova linha no output 
    
    return resposta

def flatten(lst: list):
    """ Recebe uma lista e retorna uma copia achatada """

    resposta = [] #output

    for valor in lst:
        if type(valor) is list: #se o valor eh uma nova lista, chama recursivamente a funcao para extender no output
            recursao = flatten(valor) #recursivo pois pode ter uma outra lista depois
            resposta.extend(recursao)
        else: #se nao, so adiciona
            resposta.append(valor)

    return resposta
        


if __name__ == "__main__" :
    teste1 = [1, 2, -5, 4, 7, 1, 2]
    print(pares_e_impares(teste1))

    teste2 = [0, -9, 'e', 3.2, 3.5]

    print(pares_e_impares(teste2))

    teste3 = ["abcd", "a", "aaaaa", "bb", "bbbbb"]

    print(filtrar_por_tamanho(teste3, 2))

    teste4 = rotate_tuple((1, 2, 3, 4), 9)
    print(teste4)

    teste5 = transpose([[1,2,3],[4,5,6]])
    print(teste5)

    teste6 = flatten([[1,2], 3, [[4,[5]], 6], 7])
    print(teste6)
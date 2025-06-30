
def group_by(pairs: list):
    """ Recebe lista de tuplas (chave, valor) e retorna um dicionario, 
    sendo cada chave do dicionario uma chave presente nas tuplas
    e cada valor a lista de todos os valores que levam aquela chave nas tuplas """

    resp = {} #output

    for tpl in pairs:
        key = tpl[0] #capturando cada chave presente nas tuplas
        value = tpl[1] #cada valor nas tuplas

        novo_valor = resp.get(key, []) #buscando no output aquela chave para ver se ja existe, se nao inicia lista vazia
        novo_valor.append(value) #adiciona valor atual

        resp.update({key: novo_valor})

    return resp

def invert_map(d: dict):
    """ Recebe um dicionario com valores unicos e inverte chave por valor """
    resp = {} #output

    for key, value in d.items(): #percorrendo items do input
        resp.update({value: key}) #inverte chave e valor para o output

    return resp

def indices_of(lst: list):
    """ Recebe uma lista e retorna um dicionario onde cada valor da lista eh chave, 
    e o valor eh a lista de indices onde aparece """
    resp = {} #output

    for index, value in enumerate(lst): #percorrendo lista de entrada com indice e valor 

        novo_valor = resp.get(value, []) #busca no dicionario de resposta para ver se ja existe, se nao inicia com lista vazia
        novo_valor.append(index) #adiciona indice atual

        resp.update({value: novo_valor})

    return resp

def merge_dicts(dicts: list[dict]):
    """ Recebe uma lista de dicionarios e retorna um unico com seus valores juntos, 
    ou seja, se ja existe uma chave, soma os valores, se nao, adiciona a nova chave com o valor """
    resp = {} #output

    for item in dicts:

        for key, value in item.items(): #percorrendo cada dicionario
            valor_atual = resp.get(key) #busca se ja existe a chave no output
            novo_valor = value #novo valor carregado com valor da iteracao

            if valor_atual != None: #se ja existe, soma
                novo_valor += valor_atual
            
            resp.update({key: novo_valor})

    
    return resp

def conta_digitos(n: int):
    """ Recebe um inteiro e retorna um dicionario com chaves de 0-9 e valores com quantas vezes
    apareceu cada digito na representacao decimal """

    numero_positivo = abs(n) #input como positivo

    resp = {} #output

    for counter in range(10):
        resp.update({str(counter): 0}) #adicionando ao output os valores de 0 a 9 como chave, iniciando com valor 0

    for digito in str(numero_positivo): #para pegar a representacao decimal, convertendo para string o input e percorrendo
        valor_atual = resp.get(digito) #valor atual de repeticoes no dicionario
        novo_valor = valor_atual + 1 #soma 1

        resp.update({digito: novo_valor})

    return resp


if __name__ == "__main__" :
    print(group_by([("A", 1), ("B", 2), ("B", 1), (1, 2), (1, "a")]))

    print(invert_map({'a':  1, 'b':2}))

    print(indices_of([1,1,2,7,1]))

    print(merge_dicts([{'a':  1, 'b':2}, {'c': 1, 'd': 7, 'a': 1}, {'d': 2}]))

    print(conta_digitos(-999))
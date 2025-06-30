import itertools



def portfolio_combinations(assets: list[str], k: int) -> int:
    """
    Calcula as combinações de tamanho k de assets possiveis

    Parameters:
        assets: lista de ativos
        k: tamanho de cada combinação

    Returns:
        int: numero de combinações
    """

    combinacoes = list(itertools.combinations(assets, k)) #cria todas as combinacoes com a lista de entrada

    return len(combinacoes)


def moving_average(prices: list[float], window: int) -> list[float]:
    """
    Retorna uma lista de medias para cada janela deslizante de comprimento window

    Parameters:
        prices: lista de precos
        window: tamanho da janela

    Returns:
        list[float]: lista de medias
    """
    output = []
    iters = itertools.tee(prices, window) #criando window iteradores da lista

    for i, it in enumerate(iters): #dando offset crescente em cada iterador, ate window
        for _ in range(i):
            next(it, None)

    #desempacota lista de iteradores e agrupa valores em cada posicao, criando tuplas de tamanho igual ao menor iterador
    #ou seja, de tamanho window se window <= len(prices), se nao, tamanho 0
    zip_iteradores = zip(*iters) 

    for tupla in zip_iteradores:  #para cada tupla
        output.append(sum(tupla) / window) #adiciona a media no output

    return output






if __name__ == "__main__" :
    # print(portfolio_combinations(['a', 'b', 'c', 'd'], 2))
    print(moving_average([1,2,3,4,5], 2))
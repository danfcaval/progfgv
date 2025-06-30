import random


def simulate_stock_price(initial_price: float, mu: float, sigma: float, days: int) -> list[float]:
    """
    Simula variações de preço utilizando distribuicao normal

    Parameters:
        initial_price: preço inicial do ativo
        mu: média
        sigma: desvio padrão
        days: dias de variação

    Returns:
        list[float]: lista de tamanho days com as variacoes calculadas


    """
    precos = [initial_price]

    for _ in range(days):
        variacao_diaria = random.gauss(mu, sigma)
        novo_preco = precos[-1] + variacao_diaria #ultimo valor da lista de precos (dia anterior) + variacao de hoje
        precos.append(novo_preco)

    return precos



if __name__ == "__main__" :
    print(simulate_stock_price(100.0, 0.0, 1.0, 2))
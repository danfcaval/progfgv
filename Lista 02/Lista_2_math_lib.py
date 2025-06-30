import math

def future_value(pv: float, r: float, n: int, t: float) -> float:
    """
    Calcula valor futuro

    Parameters:
        pv: valor presente
        r: taxa de juros anual
        n: periodos por ano
        t: tempo em anos

    Returns:
        float: valor futuro
    """

    fator_desconto = pow((1 + r/n), n * t)
    valor_futuro = pv * fator_desconto

    return valor_futuro


def standard_deviation(returns: list[float]) -> float:
    """
    
    Calcula o desvio padrao das entradas

    Parameters:
        returns: lista de numeros

    Returns:
        float: desvio padrao
    """

    valor_total = math.fsum(returns)
    numero_retornos = len(returns)
    media = valor_total / numero_retornos

    soma_n = 0 #parte direita do calculo do desvio

    for i in range(numero_retornos):
        soma_n += (returns[i] - media) ** 2

    total_inverso = 1/numero_retornos

    desvio_padrao = math.sqrt(total_inverso * soma_n)

    return desvio_padrao

def time_to_double(r: float) -> float:
    """
    Calcula o tempo para dobrar o valor em capitalizacao continua

    Parameters:
        r: taxa
    
    Returns:
        float: numero de anos para dobrar investimento
    """

    return math.log(2) / math.log(1 + r)

if __name__ == "__main__" :
    #print(future_value(1000000.0, 0.12, 12, 1))
    #print(standard_deviation([45, 3, 22.2]))
    print(time_to_double(.5))


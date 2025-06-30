import numpy as np

def simular_precos(S0: float, sigma: float, days: int) -> np.ndarray:
    """
    Retorna um np.ndarray de tamanho days + 1, onde o primeiro elemento e S0 e, a cada passo
    soma-se um ruido normal de desvio padrao sigma

    Parameters:
        S0: preco inicial positivo
        sigma: desvio padrao do ruido
        days: numero de dias a simular

    Returns:
        np.ndarray: array com variacoes do ruido
    """

    #gera ruido normal de desvio padrao sigma e tamanho days
    ruidos = np.random.normal(loc=0.0, scale=sigma, size=days)
    
    #inicializa com o valor inicial
    precos = np.empty(days + 1)
    precos[0] = S0
    
    #preenche o output com a soma do ruido a cada passo
    for t in range(0, days):
        precos[t + 1] = precos[t] + ruidos[t]
    
    return precos

def calc_retornos_simples(prices: np.ndarray) -> np.ndarray:
    """
    Calcula os retornos simples diarios a partir de uma serie de precos

    Formula:
        r_t = (P_t - P_{t-1}) / P_{t-1}

    Parameters:
        prices: vetor de precos

    Returns:
        np.ndarray: retornos simples diarios
    """

    #percorrendo o array de entrada, da posicao 1 ate o fim - posicao 0 ate a penultima
    #dividido pela posicao 0 ate a penultima
    return (prices[1:] - prices[:-1]) / prices[:-1]

def calc_retornos_log(prices: np.ndarray) -> np.ndarray:
    """
    Calcula os log-retornos diarios a partir de uma serie de precos.

    Formula:
        r_t^log = ln(P_t / P_{t-1})

    Parameters:
        prices: vetor de precos

    Returns:
        np.ndarray: log-retornos diarios
    """
    #log da posicao 1 ate o fim, dividido pela posicao 0 ate a penultima
    return np.log(prices[1:] / prices[:-1])

def sma(returns: np.ndarray, window: int) -> np.ndarray:
    """
    Calcula a media movel simples para um vetor de retornos

    Formula:
        SMA_t = (1 / window) * sum_{i=t-window+1}^t r_i

    Parameters:
        returns: vetor de retornos
        window: tamanho da janela

    Returns:
        np.ndarray: vetor da media movel
    """
    result = []

    for t in range(window - 1, len(returns)):
        janela = returns[t - window + 1: t + 1]
        media = np.mean(janela)
        result.append(media)

    return np.array(result)

def rolling_std(returns: np.ndarray, window: int, days_size: int = 0) -> np.ndarray:
    """
    Calcula o desvio padrao movel para um vetor de retornos.

    Formulas:
        r_t = media dos retornos na janela
        sigma_t = sqrt(1 / (window - days_size) * sum_{i=t-window+1}^t (r_i - r_t)^2)

    Parameters:
        returns: vetor de retornos
        window: tamanho da janela
        days_size: ajuste da normalizacao

    Returns:
        np.ndarray: vetor do desvio padrao movel
    """
    denominador = window - days_size

    #calculando media movel com convolucao entre vetores
    media_movel = np.convolve(returns, np.ones(window)/window, mode='valid')
    
    result = []

    #calculando sigma com somatorio
    for t in range(len(media_movel)):
        window_slice = returns[t:t+window]
        media = media_movel[t]
        std = np.sqrt(np.sum((window_slice - media) ** 2) / denominador)
        result.append(std)
    
    return np.array(result)

if __name__ == "__main__" :
    print(simular_precos(50.0, 3.0, 5))

    prices = np.array([100, 110, 102, 95, 143])
    print(calc_retornos_simples(prices))
    print(calc_retornos_log(prices))
    print(sma(calc_retornos_simples(prices), window=3))
    print(rolling_std(calc_retornos_simples(prices), window=3))
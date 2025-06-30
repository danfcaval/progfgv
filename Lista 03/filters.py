import numpy as np

def replace_negatives(v: np.ndarray, new_value: float) -> np.ndarray:
    """
    Dado um vetor v, cria uma copia e substitui cada entrada negativa por new_value

    Parameters:
        v: vetor numpy 1D.
        new_value: valor que substituira cada elemento negativo

    Returns:
        np.ndarray: novo vetor numpy com as substituições feitas.
    """

    result = v.copy()
    
    #para cada entrada, valida a condicao e substitui
    for i in range(len(result)):
        if result[i] < 0:
            result[i] = new_value
    
    return result


def local_peaks(series: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Encontra todos os maximos locais em uma serie temporal unidimensional

    Parameters:
        series: vetor numpy 1D com pelo menos 3 elementos

    Retorno:
        tuple:
            vetor dos indices dos maximos locais
            vetor dos valores correspondentes dos maximos locais
    """

    indices = []
    peaks = []
    
    #percorrendo a serie do segundo ao penultimo elemento, e adicionando ao output caso condicao de maximo local atingida
    for t in range(1, len(series) - 1):
        if series[t] > series[t-1] and series[t] > series[t+1]:
            indices.append(t)
            peaks.append(series[t])
    
    return np.array(indices), np.array(peaks)

if __name__ == "__main__":
    print(replace_negatives(np.array([5, -5, 5, -1, 5]), 0))
    print(local_peaks(np.array([1, 3, 1, 7, 7, 5, 4])))
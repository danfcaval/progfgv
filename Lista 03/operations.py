import numpy as np

def rotate_90(A: np.ndarray) -> np.ndarray:
    """
    Rotaciona uma matriz quadrada 90 graus no sentido horario

    Parameters:
        A: matriz quadrada

    Returns:
        np.ndarray: matriz rotacionada
    """
    n, m = A.shape

    transposta = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            transposta[j][i] = A[i][j]

    rotacionada = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            rotacionada[i][j] = transposta[i][n - 1 - j]

    return rotacionada

def sum_subdiagonals(A: np.ndarray, k: int) -> float:
    """
    Calcula a soma dos elementos da k subdiagonal de uma matriz quadrada

    A subdiagonal k corresponde aos elementos A[i, i - k] com i de k ate n - 1

    Parameters:
        A: matriz quadrada
        k: indice da subdiagonal, com 1 ≤ k < n

    Returns:
        float: soma dos elementos da subdiagonal k

    Raises:
        ValueError: se k nao estiver no intervalo correto, ou a matriz nao for quadrada
    """
    n, m = A.shape
    if n != m:
        raise ValueError("A matriz deve ser quadrada.")
    if not (1 <= k < n):
        raise ValueError("k deve estar no intervalo 1 ≤ k < n.")
    
    soma = 0.0
    for i in range(k, n):
        j = i - k  # posicao da coluna na subdiagonal k
        soma += A[i][j]

    return soma

def block_matmul(A: np.ndarray, B: np.ndarray, block_size: int) -> np.ndarray:
    """
    Realiza a multiplicacao de matrizes A e B por blocos

    Divide as matrizes A e B em blocos de tamanho block_size
    e computa o produto em blocos acumulando os resultados

    Parameters:
        A: matriz
        B: matriz
        block_size: tamanho do bloco

    Returns:
        np.ndarray: matriz resultado do produto em blocos

    Raises:
        ValueError: se as dimensoes forem incompativeis
    """
    n, p = A.shape
    p2, m = B.shape
    if p != p2:
        raise ValueError("As dimensões internas de A e B devem ser compatíveis.")

    C = np.zeros((n, m))

    for i0 in range(0, n, block_size):
        for j0 in range(0, m, block_size):
            for k0 in range(0, p, block_size):
                i_max = min(i0 + block_size, n)
                j_max = min(j0 + block_size, m)
                k_max = min(k0 + block_size, p)

                A_block = A[i0:i_max, k0:k_max]
                B_block = B[k0:k_max, j0:j_max]
                C[i0:i_max, j0:j_max] += A_block @ B_block

    return C

if __name__ == "__main__" :
    print(rotate_90(np.array([[1, 2], [3, 4]])))
    print(sum_subdiagonals(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 2))
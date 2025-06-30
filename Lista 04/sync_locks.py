import threading
import time
import random

def gerenciar_risco(total_risco: float, estrategias: list[tuple[str, float]], tempo_total: int) -> dict[str, float]:
    """
    Simula alocacao de risco em diversas estrategias concorrentes de um portfolio

    Devido a como a pergunta foi formulada, depois que todo o risco foi alocado, a thread que nao conseguiu alocar
    ficara esperando ate o fim do tempo_total sem razao alguma, pois nunca sera desalocado o risco de outra estrategia

    Parameters:
        total_risco: risco maximo
        estrategias: lista de tuplas (nome da estrategia, risco desejado)
        tempo_total: tempo total

    Returns:
        dict[str, float]: dict com o risco alocado por estrategia
    """

    #risco total como lista para ter mutabilidade
    risco_disponivel = [total_risco]  

    #instanciando alocacoes
    alocacoes={}
    for nome, _ in estrategias:
        alocacoes.update({nome: 0.0})

    lock = threading.Lock()
    stop_event = threading.Event()

    #funcao que tenta alocar o risco na estrategia
    def tentar_alocar(nome: str, risco_desejado: float):
        while not stop_event.is_set():
            with lock:
                if risco_disponivel[0] >= risco_desejado:
                    risco_disponivel[0] -= risco_desejado
                    alocacoes[nome] += risco_desejado
                    return  # sucesso, sai da thread
            time.sleep(0.5)  # espera antes de tentar novamente

    threads = []
    for nome, risco in estrategias:
        t = threading.Thread(target=tentar_alocar, args=(nome, risco))
        t.start()
        threads.append(t)

    time.sleep(tempo_total)
    stop_event.set()

    for t in threads:
        t.join()

    return alocacoes

def monitorar_acoes(acoes: list[str], valor_alvo: float) -> list[str]:
    """
    Monitora variacoes de px de acoes e registra os que atingirem ou ultrapassarem valor_alvo
    
    valor_alvo entre 1 e 20, pois necessita estar entre o intervalo de precos gerados

    Parameters:
        acoes: lista de tickers
        valor_alvo: valor a ser monitorado

    Returns:
        list[str]: lista com os nomes dos tickers que atingiram ou ultrapassaram o valor_alvo
    """

    atingidas = []
    lock = threading.Lock()

    def monitorar(acao: str):
        #gerando px anterior
        preco_anterior = round(random.uniform(1, 20), 2)

        #emula latencia
        time.sleep(random.uniform(0.1, 0.3))

        #gerando px atual
        preco_atual = round(preco_anterior + random.uniform(-5, 5), 2)

        # min e max dos precos para comparar com o alvo
        minimo = min(preco_anterior, preco_atual)
        maximo = max(preco_anterior, preco_atual)

        if minimo <= valor_alvo <= maximo:
            with lock:
                atingidas.append(acao)

    threads = []
    for acao in acoes:
        t = threading.Thread(target=monitorar, args=(acao,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return atingidas

if __name__ == "__main__":
    print(gerenciar_risco(100.0, [("A", 30.0),("B", 50.0),("C", 40.0),("D", 20.0)], 5))
    print(monitorar_acoes(["BPAC11", "SANB11", "MSFT"], 15))
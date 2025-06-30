import threading
import random
from typing import Any
import time

def simular_traders(num_traders: int, num_ordens: int) -> dict[str, list[dict[str, Any]]]:
    """
    Simula multiplos traders inserindo ordens de compra e venda de forma concorrente
    
    Parameters:
        num_traders: numero de traders
        num_ordens: numero de ordens por trader
    
    Returns:
        dict[str, list[dict[str, Any]]]: dict com chaves 'buy' e 'sell' e valores com as ordens
    """
    
    order_book = {
        'buy': [],
        'sell': []
    }
    
    lock = threading.Lock()
    order_id_counter = [0] #contador como lista para ter mutabilidade

    def trader_thread():
        nonlocal order_book, lock, order_id_counter
        for _ in range(num_ordens):
            
            #lockando lista com contador para acesso seguro e atomico
            with lock:
                order_id = order_id_counter[0]
                order_id_counter[0] += 1
            
            #escolhendo buy e sell aleatoriamente
            order_type = random.choice(['buy', 'sell'])

            #escolhendo preco randomicamente em dist uniforme, arredondando pra duas casas por ser valor monetario
            price = round(random.uniform(10, 100), 2)

            #escolhendo quantidade randomicamente
            quantity = random.randint(1, 10)

            order = {
                'id': order_id,
                'price': price,
                'quantity': quantity
            }

            #lockando livro de ordens para acesso seguro e atomico
            with lock:
                order_book[order_type].append(order)

    
    threads = []

    #iniciando threads
    for _ in range(num_traders):
        t = threading.Thread(target=trader_thread)
        t.start()
        threads.append(t)
    
    #aguarda threads finalizarem
    for t in threads:
        t.join()
    
    return order_book

def simular_feeds_de_dados(acoes: list[str], tempo_total: int) -> dict[str, float]:
    """
    Simula feeds de precos de tickers concorrentes e devolve um dict com resultado

    Parameters:
        acoes: lista tickers
        tempo_total: tempo total da simulacao em segundos

    Returns:
        dict[str, float]: dicionario com precos apos a simulacao
    """

    #gerando precos randomicos em dist uniforme
    precos = {}
    for acao in acoes:
        precos.update({acao: random.uniform(1, 150)})

    lock = threading.Lock()
    #evento para sinalizar fim da simulacao para as threads
    stop_event = threading.Event()

    #funcao que ira atualizar os precos, com lock nos precos para ser atomico e sleep entre 1 a 3 segundos
    def atualizar_preco(acao: str):
        while not stop_event.is_set():
            time.sleep(random.uniform(1, 3))
            with lock:
                variacao = random.uniform(-5, 5)
                #setando precos arredondados em 2 casas, adicionando a variacao ao ultimo preco e garantindo maior que 1
                precos[acao] = round(max(1.0, precos[acao] + variacao), 2)

    #funcao que ira imprimir os precos atuais a cada 5 segundos
    def imprimir_precos():
        while not stop_event.is_set():
            time.sleep(5)
            with lock:
                atuais = {}
                for ticker, preco in precos.items():
                    atuais.update({ticker: round(preco, 2)})

                print("Precos atuais:", atuais)

    # iniciando threads
    threads = []
    for acao in acoes:
        t = threading.Thread(target=atualizar_preco, args=(acao,))
        t.start()
        threads.append(t)

    printer_thread = threading.Thread(target=imprimir_precos)
    printer_thread.start()
    threads.append(printer_thread)

    #aguarda tempo total de execucao
    time.sleep(tempo_total)
    stop_event.set()

    #aguarda threads finalizarem
    for t in threads:
        t.join()

    return precos


if __name__ == "__main__":
    print(simular_traders(2, 2))
    print(simular_feeds_de_dados(["AAPL", "GOOG", "TSLA"], 10))

import os
import urllib.request

def download_and_merge(years_quarters: list[tuple[int, int]], output_file: str) -> None:
    """
    Agrupa dados de relatorios de https://data.bls.gov/cew/data/api, para um unico arquivo,
    de acordo com input de anos e quarters

    Parameters:
        years_quarters : Lista de tuplas (ano, trimestre) para download dos dados
        output_file : Caminho do arquivo CSV de saída que conterá os dados concatenados

    Behaviour:
        Criará o diretório data/ e colocará os arquivos baixados no diretório.
        Depois irá ler todos os arquivos baixados e juntará um unico em 'output_file'.


    """

    # Cria o diretório data/ se não existir
    if not os.path.exists('data'):
        os.makedirs('data')

    # Baixa cada arquivo e salva em data/{year}_q{quarter}.csv
    for year, quarter in years_quarters:
        url = f"https://data.bls.gov/cew/data/api/{year}/{quarter}/industry/10.csv"
        nome_arquivo = f"data/{year}_q{quarter}.csv"
        urllib.request.urlretrieve(url, nome_arquivo)

    
    # Lista os arquivos CSV baixados
    # Seria melhor ja guardar o nome dos arquivos baixados no for acima, mas questao pediu assim
    arquivos = []
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            arquivos.append(os.path.join('data', file))

    # Ordena arquivos
    arquivos.sort()


    # Abre o arquivo de saída para escrita
    with open(output_file, 'w') as arquivo_out:
        primeiro_arquivo = True

        # Abre cada arquivo baixado para leitura
        for csv in arquivos:
            with open(csv, 'r') as infile:
                lines = infile.readlines()
                if primeiro_arquivo:
                    # Escreve o primeiro arquivo inteiro, incluindo cabeçalho
                    arquivo_out.writelines(lines)
                    primeiro_arquivo = False
                else:
                    # Pula a primeira linha e esceve o restante
                    arquivo_out.writelines(lines[1:])

    return output_file


if __name__ == "__main__" :
    output_file = 'teste_concatenado.csv'
    download_and_merge([(2024, 1), (2024, 2), (2024, 3), (2024, 4)], output_file)
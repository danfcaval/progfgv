

def count_anagrams(words: list[str]):
    """ Recebe lista de srings e retorna um dicionario. Cada chave eh a palavra com as letras ordenadas alfabeticamente 
    e o valor a lista de palavras que correspondem ao anagrama """

    resp = {}

    for word in words:
        chave = ''.join(sorted(word)) #ordena a palavra alfabeticamente e converte pra string

        novo_valor = resp.get(chave, []) #busca se ja existe a chave, default lista vazia para iniciar
        novo_valor.append(word) #adiciona a nova palavra

        resp.update({chave: novo_valor})

    return resp

def parse_csv(text: str, sep = ','):
    """ Recebe uma string com linhas de csv, e opcionalmente um separador, e retorna um dicionario com as chaves sendo o cabecalho
    e os valores, o valor de cada linha para tal titulo """
    resp = {} #output
    headers = [] #lista de titulos que serao as chaves
    rows = text.split('\n') #separando cada linha pela quebra de linha

    for row_index, row in enumerate(rows):
        data_list = row.split(sep) #pegando a lista de valores dando split pelo separador de valores

        for data_index, data in enumerate(data_list):
            if row_index == 0: #se for a primeira linha, sei que eh o cabecalho
                resp.update({data : []}) #preparo o output para receber adicao de valores para aquele titulo
                headers.append(data) #somo a lista de titulos
                continue
            
            new_value = resp.get(headers[data_index]) #pego valor atual no output usando a posicao do dado e minha lista de titulos

            new_value.append(data.strip()) #adiciono valor atual

            resp.update({headers[data_index]:  new_value})

    return resp

def validar_sudoku(tabuleiro: list[list[int]]):
    """ Recebe um tabuleiro de sudoku 9x9 representado por lista de listas de inteiros 
    e retorna um booleano indicando se esta valido """

    column_rule = {i: [] for i in range(9)} #dict para controlar quantas vezes cada numero apareceu em uma coluna (chave)
    square_rule = {1: [], 2: [], 3: []} #dict para separar o tabuleiro em blocos de 3, nesse caso cada chave é um grupo de colunas, que sao resetadas a cada 3 linhas
    square_rule_index = 0 #indice para saber em que bloco interagir

    for row_index, row in enumerate(tabuleiro):
        row_rule = [] #lista com os proprios valores da fileira, se limpa a cada iteracao
        
        for column, value in enumerate(row):
            if value == 0:
                continue

            if value in row_rule: #verificar se ja tinha na linha
                return False
            
            row_rule.append(value)

            column_current = column_rule.get(column) #busca a lista de valores daquela coluna pelo indice
            
            if value in column_current: #verificar se ja tinha na coluna
                return False

            column_current.append(value)
            column_rule.update({column: column_current}) #atualizar dict com novo valor

            if column < 3: #decisao de qual bloco de 3 interagir
                square_rule_index = 1
            elif column < 6:
                square_rule_index = 2
            else:
                square_rule_index = 3

            square_current = square_rule.get(square_rule_index)

            if value in square_current: #verificar se ja tinha no bloco de 3
                return False
            
            square_current.append(value)
            square_rule.update({square_rule_index: square_current}) #atualizar dict com novo valor

        if row_index in [2, 5]: 
            square_rule.update({1: [], 2: [], 3: []}) #nas linhas 2 e 5, podemos considerar novos blocos de 3x3


    return True




    







if __name__ == "__main__" :
    print(count_anagrams(["bolo", "lobo"]))

    print(parse_csv("Altura, Nome, Idade \n177, Pedro, 21\n191, Carlos, 33\n169, Alice, 23"))

    tabuleiro = [
        [0, 0, 0, 0, 9, 0, 2, 0, 0],
        [4, 0, 0, 1, 0, 0, 0, 0, 7],
        [0, 0, 3, 0, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 8, 0, 6, 0, 0, 0],
        [1, 0, 0, 0, 2, 0, 0, 7, 0],
        [0, 2, 0, 0, 0, 0, 7, 0, 0],
        [7, 0, 0, 0, 0, 9, 0, 0, 6],
        [0, 0, 6, 0, 3, 0, 0, 0, 0]
    ]

    print(validar_sudoku(tabuleiro))
# algoritmos.py

def ordenar_por_temperatura(lista_de_dados):
    """Algoritmo Merge Sort para ordenar os focos do mais quente para o menos quente."""
    if len(lista_de_dados) <= 1:
        return lista_de_dados

    meio = len(lista_de_dados) // 2
    metade_esquerda = ordenar_por_temperatura(lista_de_dados[:meio])
    metade_direita = ordenar_por_temperatura(lista_de_dados[meio:])

    return juntar_as_metades(metade_esquerda, metade_direita)


def juntar_as_metades(esquerda, direita):
    """Função auxiliar para organizar e misturar as duas partes da lista."""
    resultado_final = []
    ponteiro_esq = 0
    ponteiro_dir = 0

    while ponteiro_esq < len(esquerda) and ponteiro_dir < len(direita):
        if esquerda[ponteiro_esq]['temperatura'] > direita[ponteiro_dir]['temperatura']:
            resultado_final.append(esquerda[ponteiro_esq])
            ponteiro_esq += 1
        else:
            resultado_final.append(direita[ponteiro_dir])
            ponteiro_dir += 1

    resultado_final.extend(esquerda[ponteiro_esq:])
    resultado_final.extend(direita[ponteiro_dir:])
    return resultado_final


def busca_binaria_por_id(lista_organizada, id_procurado):
    """Algoritmo de Busca Binária para achar um foco pelo número de identificação."""
    limite_baixo = 0
    limite_alto = len(lista_organizada) - 1

    while limite_baixo <= limite_alto:
        meio = (limite_baixo + limite_alto) // 2

        if lista_organizada[meio]['id'] == id_procurado:
            return lista_organizada[meio]
        elif lista_organizada[meio]['id'] < id_procurado:
            limite_baixo = meio + 1
        else:
            limite_alto = meio - 1

    return None
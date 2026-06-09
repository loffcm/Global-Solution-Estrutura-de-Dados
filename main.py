import json
from estruturas import FilaDeFocos
from algoritmos import ordenar_por_temperatura, busca_binaria_por_id

# Dados reais fictícios simulando satélites de monitoramento do INPE
dados_dos_satelites = [
    {"id": 102, "estado": "Amazonas", "temperatura": 45.2, "satelite": "AQUA"},
    {"id": 105, "estado": "Mato Grosso", "temperatura": 52.8, "satelite": "TERRA"},
    {"id": 101, "estado": "Pantanal", "temperatura": 39.1, "satelite": "GOES-16"},
    {"id": 104, "estado": "Pará", "temperatura": 61.4, "satelite": "NOAA-20"},
    {"id": 103, "estado": "Maranhão", "temperatura": 48.0, "satelite": "METOP"}
]


def salvar_relatorio_no_computador(dados_processados, nome_do_arquivo="historico_incendios.json"):
    """Salva os dados gerados em um arquivo físico no computador (Requisito de Manipulação de Arquivos)."""
    try:
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_processados, arquivo, indent=4, ensure_ascii=False)
        print(f"\n[SUCESSO] Relatório salvo no arquivo: '{nome_do_arquivo}'")
    except IOError as erro:
        print(f"\n[ERRO] Não foi possível salvar o arquivo: {erro}")


def iniciar_sistema():
    print("=" * 60)
    print("SISTEMA DE MONITORAMENTO AMBIENTAL ESPACIAL - GLOBAL SOLUTION")
    print("=" * 60)

    try:
        # 1. Testando a Fila (Inserindo dados)
        print("\n[PASSO 1] Enviando dados brutos dos satélites para a Fila de Processamento...")
        fila_inpe = FilaDeFocos()
        for foco in dados_dos_satelites:
            fila_inpe.entrar_na_fila(foco)

        print(f"-> Fila criada com sucesso! Existem {fila_inpe.tamanho_da_fila()} focos aguardando análise.")

        # Retirando da fila e jogando para uma lista temporária para podermos trabalhar
        lista_para_analisar = []
        while not fila_inpe.esta_vazia():
            lista_para_analisar.append(fila_inpe.sair_da_fila())

        # 2. Testando a Ordenação (Merge Sort)
        print("\n[PASSO 2] Ordenando os focos por criticidade (Maior temperatura primeiro)...")
        focos_ordenados_por_calor = ordenar_por_temperatura(lista_para_analisar)

        for item in focos_ordenados_por_calor:
            print(f"Estado: {item['estado']} | Temperatura: {item['temperatura']}°C | Satélite: {item['satelite']}")

        # 3. Gravando os dados em arquivo externo
        salvar_relatorio_no_computador(focos_ordenados_por_calor)

        # 4. Testando a Busca Binária
        print("\n[PASSO 4] Executando Busca Binária inteligente por ID...")
        # A busca binária precisa que a lista esteja em ordem crescente de IDs para funcionar
        lista_ordenada_por_id = sorted(lista_para_analisar, key=lambda x: x['id'])

        id_que_eu_quero = 104
        resultado_da_busca = busca_binaria_por_id(lista_ordenada_por_id, id_que_eu_quero)

        if resultado_da_busca:
            print(f"🎉 Registro Encontrado! Detalhes: {resultado_da_busca}")
        else:
            print(f"❌ Registro com o ID {id_que_eu_quero} não foi localizado no sistema.")

    except Exception as erro_geral:
        print(f"\n[ERRO CRÍTICO] Ocorreu um problema inesperado no sistema: {erro_geral}")


# Comando que faz o Python iniciar o programa acima automaticamente ao clicar em rodar
if __name__ == "__main__":
    iniciar_sistema()
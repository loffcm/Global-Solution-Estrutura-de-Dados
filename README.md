# Global-Solution-Estrutura-de-Dados

# Sistema de Monitoramento Espacial de Focos de Calor 🛰️🔥

## 📋 Descrição do Projeto e Objetivo
Este projeto foi desenvolvido para a entrega da Global Solution da disciplina de Estruturas de Dados. A aplicação visa solucionar um problema real dentro da **Economia Espacial**: o monitoramento, organização e triagem de focos de incêndio e calor no território brasileiro, utilizando dados simulados baseados nos padrões do INPE (Instituto Nacional de Pesquisas Espaciais). O objetivo é ordenar os focos mais críticos para otimizar a tomada de decisão das brigadas de incêndio e permitir a busca ágil de registros de satélites.

## 👥 Integrantes do Grupo
* **Caio M. Lins** - RM: 559805
* **Guilherme Augusto** - RM: 562107
* **Murilo Bez Chleba** - RM: 566199
* **Bernardo Lozório** - RM: 564943

## 🎥 Vídeo de Apresentação da Solução
* **Link do Vídeo no YouTube:** https://youtu.be/2ck0NIl-p1s?si=Gyy9a2cKo_Cb02g0

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python 3.x** (Utilizando apenas recursos nativos para garantir o foco no desenvolvimento dos algoritmos puros).
* **JSON** (Para persistência, salvamento e manipulação da base de dados de histórico).

## 🏗️ Estruturas de Dados Implementadas
* **Fila Dinâmica (Queue):** Implementada manualmente (do zero) utilizando o conceito de Nodos/Elementos na unha (arquivo `estruturas.py`). Garante a lógica **FIFO** (*First-In, First-Out*), organizando os dados dos satélites rigorosamente por ordem de chegada.

## ⚡ Algoritmos Utilizados
* **Algoritmo de Ordenação — Merge Sort (`ordenar_por_temperatura`):** Algoritmo baseado em divisão e conquista implementado do zero para ordenar os focos de calor por temperatura de forma decrescente (mais graves primeiro).
* **Algoritmo de Busca — Busca Binária (`busca_binaria_por_id`):** Implementado manualmente para localizar de forma instantânea e eficiente qualquer registro de foco através do seu ID único indexado.

## ⚙️ Explicação do Funcionamento
1. O sistema simula a chegada de dados brutos de múltiplos satélites orbitais.
2. Esses dados entram na **Fila** e são descarregados em ordem cronológica.
3. O algoritmo **Merge Sort** entra em ação e reorganiza toda a lista colocando os focos com maior temperatura no topo.
4. O sistema gera e salva um arquivo físico chamado `historico_incendios.json` com os dados processados.
5. A **Busca Binária** é utilizada para pesquisar rapidamente um foco específico digitando apenas o número do seu ID.

## 🚀 Instruções de Execução
1. Certifique-se de ter o Python 3 instalado no computador.
2. Baixe os arquivos `estruturas.py`, `algoritmos.py` e `main.py` e coloque-os no mesmo diretório.
3. Abra o terminal ou prompt de comando na pasta dos arquivos e execute:
   ```bash
   python main.py

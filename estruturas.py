class Elemento:
    """Representa um único dado (foco de incêndio) dentro da nossa estrutura."""
    def __init__(self, conteudo):
        self.conteudo = conteudo  # Guarda as informações do foco de calor
        self.proximo = None       # Aponta para o próximo elemento da fila

class FilaDeFocos:
    """Fila criada do zero para organizar os dados que chegam dos satélites."""
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self._total = 0

    def entrar_na_fila(self, conteudo):
        """Adiciona um novo foco de calor no final da fila."""
        novo_elemento = Elemento(conteudo)
        if self.ultimo is None:
            self.primeiro = novo_elemento
            self.ultimo = novo_elemento
        else:
            self.ultimo.proximo = novo_elemento
            self.ultimo = novo_elemento
        self._total += 1

    def sair_da_fila(self):
        """Remove e retorna o foco que está há mais tempo na fila (o primeiro)."""
        if self.esta_vazia():
            return None
        temporario = self.primeiro
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None
        self._total -= 1
        return temporario.conteudo

    def esta_vazia(self):
        """Diz se a fila está sem nenhum elemento."""
        return self.primeiro is None

    def tamanho_da_fila(self):
        """Retorna a quantidade de elementos na fila."""
        return self._total
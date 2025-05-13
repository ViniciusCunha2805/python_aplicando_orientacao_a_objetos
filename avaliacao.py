# Define a classe Avaliacao, usada para representar a nota que um cliente dá a um restaurante
class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente  # Nome do cliente que fez a avaliação
        self._nota = nota        # Nota que o cliente deu (espera-se que seja entre 1 e 5)

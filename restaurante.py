from python_aplicando_orientacao_a_objetos.avaliacao import Avaliacao
from python_aplicando_orientacao_a_objetos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    # Lista onde ficam todos os restaurantes criados
    restaurantes = []

    def __init__(self, nome, categoria):
        # Guarda o nome e a categoria do restaurante
        self._nome = nome
        self._categoria = categoria

        # Começa fechado (inativo)
        self._ativo = False

        # Guarda as notas que o restaurante vai receber
        self._avaliacao = []

        # Guarda os alimentos do cardápio
        self._cardapio = []

        # Adiciona esse restaurante na lista geral
        Restaurante.restaurantes.append(self)

    def __str__(self):
        # Mostra o nome e a categoria quando der print no restaurante
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        # Mostra todos os restaurantes da lista
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")

        # Para cada restaurante, mostra os dados dele
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | "
                  f"{restaurante._categoria.ljust(25)} | "
                  f"{str(restaurante.media_avaliacoes).ljust(25)} | "
                  f"{restaurante.ativo}")

    @property
    def ativo(self):
        # Mostra ⌧ se estiver aberto, ou ☐ se estiver fechado
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        # Troca o estado: se estava fechado, abre; se estava aberto, fecha
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        # Se a nota for entre 1 e 5, guarda a avaliação
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        # Se ninguém avaliou ainda, mostra "-"
        if not self._avaliacao:
            return '-'
        
        # Soma as notas e calcula a média
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)  # arredonda pra 1 casa decimal
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'_descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)

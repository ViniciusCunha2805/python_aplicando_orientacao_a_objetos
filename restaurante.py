from python_aplicando_orientacao_a_objetos.avaliacao import Avaliacao 

class Restaurante:
    # Lista que vai guardar todos os restaurantes criados
    restaurantes = []

    def __init__(self, nome, categoria):
        # Atributos do restaurante (privados por convenção com "_")
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []

        # Toda vez que um novo restaurante é criado, ele é adicionado à lista da classe
        Restaurante.restaurantes.append(self)

    def __str__(self):
        # Quando imprimir o restaurante, vai aparecer "nome | categoria"
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        # Esse método usa "cls" porque está acessando a LISTA da CLASSE, e não um objeto específico
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")

        # Para cada restaurante salvo na lista da classe...
        for restaurante in cls.restaurantes:
            # ...mostra o nome, a categoria e o status (ativo ou não)
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}")

    @property # Transforma uma função em um atributo de leitura
    def ativo(self):
        # Quando alguém pedir restaurante.ativo, vai retornar ⌧ se estiver ativo, ou ☐ se não
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
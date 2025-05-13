class Restaurante:
    # Lista que vai guardar todos os restaurantes criados
    restaurantes = []

    def __init__(self, nome, categoria):
        # Atributos do restaurante (privados por convenção com "_")
        self._nome = nome
        self._categoria = categoria
        self._ativo = False

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

# Criando três restaurantes (eles vão automaticamente pra lista da classe)
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza express', 'Italiana')
restaurante_hamburguer = Restaurante('Comelao', 'Podrao')
restaurante_praca.alternar_estado()

# Chamando o método da CLASSE para listar todos os restaurantes criados
Restaurante.listar_restaurantes()

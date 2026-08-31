# Simular um sistema de batalha entre personagens de um RPG. SUPERCLASSE Personagem
# {abstract} ATRIBUTOS nome, vida, golpes, e MÉTODOS atacar(alvo, forca), receber
# dano(dano), curar() {abstract}. SUBCLASSES Guerreiro com o MÉTODOS curar() e Mago curar().

from abc import ABC, abstractmethod
import random
from rich import print


class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        # Cada personagem terá sua própria lista de golpes
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        # Novidade: o parâmetro de um MÉTODOS pode ser a INSTÂNCIA de um OBJETO
        # No exemplo abaixo, o parâmetro 'alvo' do métodos 'atacar' faz isso
        if self.vida > 0 and alvo.vida > 0:
            # Sorteia um dos golpes da lista do personagem
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'{self.nome} ({self.vida}) atacando {alvo.nome} ({alvo.vida}) com {golpe} de força {forca}')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque de {self.nome} em {alvo.nome} não pode acontecer')



    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f'{self.nome} recebeu dano de {fator}')

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Murro no Rosto', 'Super Empurrão', 'Chute Giratório']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'{self.nome} passou emplastro e recuperou {fator} pontos de vida')


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Raio Hipnótico', 'Zumbido Ensurdecedor',
                       'Olhar Paralisante']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'{self.nome} tomou elixir e recuperou {fator} pontos de vida')

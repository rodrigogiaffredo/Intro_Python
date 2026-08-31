# Polimorfismo de INCLUSÃO usando animais como exemplo

# Pato, Cachorro, Gato, Galinha

# Todos podem ter um mesmo método chamado 'emitir_som()' porém com resultados totalmente diferentes.

# Posso usar herança para criar uma SUPERCLASSE abstrata Animal() com um método emitir_som() e portanto
# todas as SUBCLASSES terão que emitir som.

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome:str=''):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f'{self.nome} é {self.__class__.__name__} e está emitindo um som')



class Pato(Animal):
    # Apesar de a SUPERCLASSE 'Animal' possuir o método 'emitir_som', posso criar um exclusivo para
    # a SUBCLASSE 'Pato'.
    # Mesmo nome do método, resultado diferente.
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer QUACK! QUACK!')
    


class Cachorro(Animal):
    # Apesar de a SUPERCLASSE 'Animal' possuir o método 'emitir_som', posso criar um exclusivo para
    # a SUBCLASSE 'Cachorro'.
    # Mesmo nome do método, resultado diferente.
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer AU! AU! AU!')


# Posso ainda fazer com que raças diferentes de cachorros herdem de 'Cachorro' e possam emitir sons
# diferentes

class Spitz(Cachorro):
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer au!au!au!au!au!au!au!au!au!au!au!au!au!au!au!')

class PitBull(Cachorro):
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer RUF! RUF! RUF!')


class Gato(Animal):
    # Apesar de a SUPERCLASSE 'Animal' possuir o método 'emitir_som', posso criar um exclusivo para
    # a SUBCLASSE 'Gato'.
    # Mesmo nome do método, resultado diferente.
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer MIAU! MIAU!')


class Galinha(Animal):
    # Apesar de a SUPERCLASSE 'Animal' possuir o método 'emitir_som', posso criar um exclusivo para
    # a SUBCLASSE 'Galinha'.
    # Mesmo nome do método, resultado diferente.
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer PÓ! PÓ! PÓ!')
    


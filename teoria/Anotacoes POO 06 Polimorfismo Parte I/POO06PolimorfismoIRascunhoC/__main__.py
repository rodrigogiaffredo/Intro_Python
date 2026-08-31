
# Polimorfismo de INCLUSÃO usando animais como exemplo

# Pato, Cachorro, Gato, Galinha

# Todos podem ter um mesmo método chamado 'emitir_som()' porém com resultados totalmente diferentes.

from animais import *

def main():
    a1 = Cachorro('Bandit')
    # Sem o método definido em 'Cachorro' a resposta era a definida em 'Animal'
    a1.emitir_som()
    a2 = Gato('Frajola')
    # Sem o método definido em 'Gato' a resposta era a definida em 'Animal'
    a2.emitir_som()
    a3 = Pato('Donald')
    # Sem o método definido em 'Pato' a resposta era a definida em 'Animal'
    a3.emitir_som()
    a4 = Galinha('Pintadinha')
    # Sem o método definido em 'Galinha' a resposta era a definida em 'Animal'
    a4.emitir_som()
    c1 = Spitz('Luluzinha')
    # Sem o método definido em 'Spitz' a resposta era a definida em 'Cachorro'
    c1.emitir_som()      
    c2 = PitBull('Guerreiro')
    # Sem o método definido em 'PitBull' a resposta era a definida em 'Cachorro'
    c2.emitir_som()


if __name__ == '__main__':
    main()


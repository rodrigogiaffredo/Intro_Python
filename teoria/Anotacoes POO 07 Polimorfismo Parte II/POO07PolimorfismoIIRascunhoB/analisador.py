
# A importação do single dispatch method permite a sobrecarga de métodos, caso contrário ao usarmos
# o mesmo nome em métodos diferentes, sempre que for chamado no código, será executada a tarefa
# do último método criado.

from functools import singledispatchmethod

# O single dispatch method valida somente o disparo do primeiro parâmetro (single).
# Para múltiplos parâmetros, temos que usar multiple dispatch method, via biblioteca externa.


class Analisador:

    @singledispatchmethod
    # Caso o tipo não seja reconhecido durante a análise por não estar contido em @analisar.register
    def analisar(self, valor):
        print(f'Não foi possível analisar o valor {valor}.')


    @analisar.register
    # O símbolo '_' representa o nome 'analisar' definido em @nome.register
    def _(self, valor: int):
        print(f'O valor {valor} é um número inteiro.')


    @analisar.register
    def _(self, valor: str):
        print(f'O conteúdo {valor} é uma cadeia de caracteres.')


    @analisar.register
    def _(self, valor: tuple|list|dict):
        print(f'O conteúdo {valor} é uma coleção de dados.')


    @analisar.register
    def _(self, valor: float):
        print(f'O valor {valor} é um número com ponto flutuante (Real).')




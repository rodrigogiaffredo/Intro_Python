# Criar uma classe Livro que vai simular  a passagem de páginas de um livro, considerando
# também se o usuário chegou ao fim da leitura.

from rich import print
from time import sleep


class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.totalpaginas = paginas
        self.paginaatual = 1
        print(f':open_book: Você acabou de abrir o livro "{self.titulo}" que contém '
              f'{self.totalpaginas} páginas. Você está na página {self.paginaatual}.')

    def avancarpaginas(self, qtd = 1):
        cont = 0
        for pagina in range(0, qtd, 1):
            if not self.fimdolivro():
                self.paginaatual += 1
                print(f'Pág {self.paginaatual} :arrow_forward:', end = ' ')
                sleep(0.1)
                cont += 1
        print(f'Você avançou {cont} páginas e está na página {self.paginaatual}.')
        if self.fimdolivro():
            print(f':closed_book: Você chegou ao final do livro "{self.titulo}".')

    def fimdolivro(self) -> bool:
        return True if self.paginaatual == self.totalpaginas else False




# Declaração de OBJETO
livro1 = Livro('Aprendendo Python', 20)
livro1.avancarpaginas(10)
livro1.avancarpaginas(5)
livro1.avancarpaginas(35)
livro1.avancarpaginas(17)

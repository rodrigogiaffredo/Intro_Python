# Criar um código em Python que teste se o site Folha de São Paulo está acessível
# pelo computador usado. Usa try except também mas tem novidade. Tive que pesquisar mesmo
# como fazer, o professor até sugeriu, então tome NotebookLM.


import urllib
import urllib.request

def site(url):
    try:
        site = urllib.request.urlopen(url)
    except Exception as erro:
        print(f'Não consegui acessar o site {url} ({erro}).')
    else:
        print(f'O site {url} ESTÁ acessível no momento.')
        print()
        # Bônus da aula - acessando o código 'html' do site (deixei como comentário porque
        # é uma quantidade gigante de código).
        # print(site.read())


# Programa principal
site('http://www.folha.com.br/')

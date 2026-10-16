

# Implementar um exportador de dados funcional para JSON e XML.

# CLASSES

# ----------            ------------
# ALUNO                 USUARIO
# ----------            ------------
# + nome                + nome
# + curso               + email
# + serie               ------------
# ----------            ------------
# ----------


# As classes ALUNO e USUARIO usam serviços das classes JSON e XML (dependência)


# -------------         ------------
# JSON                  XML
# -------------         ------------
# -------------         ------------
# + exportar()          + exportar()
# -------------         ------------


from json import dumps
import xml.etree.ElementTree as ET


class Usuario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email



class Aluno:

    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class JSON:

    def exportar(self, dados):

        print('Exportando JSON...')

        lista = []
        for item in dados:
            lista.append(item.__dict__)

        txt = dumps(lista, ensure_ascii=False, indent=2)
        return txt
    




class XML:

    def exportar(self, dados):

        print('Exportando XML...')

        nome = dados[0].__class__.__name__.lower()
        pai = ET.Element('dados')
        for item in dados:
            filho = ET.SubElement(pai, nome)
            for chave, valor in item.__dict__.items():
                neto = ET.SubElement(filho, chave)
                neto.text = str(valor)
        ET.indent(pai, space='\t')
        txt = ET.tostring(pai, encoding='unicode', xml_declaration=True)
        return txt


    


def exportar_dados(formato, dados):
    print(formato.exportar(dados))












# Criar classes para validadores de dados, com os exemplos a seguir:


# SUPERCLASSE

# -----------
# Validador {abstract}
# -----------
# -----------
# + validar()
# -----------


# SUBCLASSES

# ----------            --------------          ------------
# Usuario               Email                   Senha
# ----------            --------------          ------------
# ----------            --------------          ------------
# ----------            --------------          ------------




# Regras de usuário:
# - de 5 a 20 caracteres
# - letras minúsculas
# - números
# - símbolo de sublinhado


# Regras de senha:
# - pelo menos 8 caracteres
# - pelo menos uma maíuscula
# - pelo menos um símbolo


# Regras de e-mail:
# - deve conter uma única @
# - usuário pode conter letras, números e alguns símbolos
# - os domínios contém pontos
# - o TLD (top level domain) encerra com ponto e pelo menos duas letras


from abc import ABC, abstractmethod
# Importação da biblioteca de EXPRESSÕES REGULARES
import re



class Validador(ABC):

    @abstractmethod
    def validar(self, valor:str) -> bool:
        pass



class Usuario(Validador):
    def validar(self, valor:str) -> bool:
        # Do mesmo jeito que temos a expressão formatada no Python (f''), temos a chamada
        # expressão REGULAR (r'')
        # Como dizer que aceito letras minúsculas de 'a' a 'z', números de 0 a 9, e o símbolo '_'
        # com tamanho de 5 a 20 caracteres
        regex = r'^[a-z0-9_]{5,20}$'
        if re.fullmatch(regex, valor):
            return True
        else:
            return False



class Email(Validador):
    def validar(self, valor:str) -> bool:
        # Agora as regras do e-mail
        regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$'
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


class Senha(Validador):
    def validar(self, valor:str) -> bool:
        # Agora as regras da senha
        regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%?]).{8,}$'
        if re.fullmatch(regex, valor):
            return True
        else:
            return False



# Método polimórfico de validação, o qual varia a depender do parâmetro passado

def validar_dado(validador: Validador, valor:str):
    resultado = validador.validar(valor)
    print(f'Valor: {valor} é válido? {'Sim' if resultado else 'Não'}')


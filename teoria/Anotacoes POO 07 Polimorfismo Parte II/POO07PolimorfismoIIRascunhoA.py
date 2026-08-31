
# POLIMORFISMO (CONTINUAÇÃO)

# A palavra polimorfismo deriva do grego Polýs (vários) Morphé (forma), e a definição nos livros de POO 
# é 'propriedade ou estado daquilo que se apresenta e/ou se composta de várias formas diferentes'.

# O professor resumiu como 'um único nome, com comportamentos diferentes'.

# Tipos de polimorfismo: inclusão (override/subtyping), sobrecarga (ad-hoc overloading), coerção (ad-hoc
# coercion) e paramétrico (template/generic).



# OVERLOAD

# Existem dois tipos de sobrecarga: a de métodos e a de operadores.

# Sobrecarga de MÉTODO: o mesmo nome de método, mas com parâmetros diferentes os quais fazem com que as
#                       tarefas executadas sejam diferentes. As assinaturas diferentes distinguem o 
#                       resultado da execução do método. No Python isso não é nativo, mas existe uma
#                       biblioteca chamada 'functools' a qual, quando importada, permite o overload
#                       de método.
#                       
#                       Exemplo:
#                       ----------------------
#                       SUPERCLASSE Analisador
#                       ----------------------
#                       ----------------------
#                       MÉTODOS
#                       analisar(int)
#                       analisar(float)
#                       analisar(str)
#                       analisar(bool)
#                       analisar(list)
#                       analisar(dict)
#                       ----------------------


# Sobrecarga de OPERADOR: manipulação do funcionamento de operadores de acordo com a necessidade do
#                         programador. Existem diversos dunder methods para isso, mas durante a aula
#                         foram abordados:

#                         Equal to                      p1 == p2        p1.__eq__(p2)
#                         Not equal to                  p1 != p2        p1.__ne__(p2)
#                         Less than                     p1 < p2         p1.__lt__(p2)
#                         Less than or equal to         p1 <= p2        p1.__le__(p2)
#                         Greater than                  p1 > p2         p1.__gt__(p2)
#                         Greater than or equal to      p1 >= p2        p1.__ge__(p2)
#                         In-place Addition             p1 += p2        p1.__iadd__(p2)
#                         In-place Substract            p1 -= p2        p1.__isub__(p2)



# DUCK TYPING

# Não é um tipo de polimorfismo, mas sim uma prática polimórfica que utiliza um método polimórfico de
# dentro de nossa biblioteca, o qual pode ser chamado independentemente de sua estrutura.

# 'Se parece com um pato, nada como um pato, voa como um pato, faz som de pato, então PROVAVELMENTE
# é um pato'.

# O Python tem um jeito próprio de executar o polimorfismo, que preconiza que não importa o tipo do 
# objeto, o que importa é se ele é capaz de ter um certo comportamento.

# Por exemplo, se imaginarmos o método 'abrir()'. Ele pode ser aplicado às classes Porta, LataAzeitona,
# ContaBancaria, Ovo, Pacote, Revista, Empresa, Cabeca (literalmente ou filosoficamente), etc.

# Para o Python, mesmo que não haja relação nenhuma entre essas classes, isso absolutamente não importa.




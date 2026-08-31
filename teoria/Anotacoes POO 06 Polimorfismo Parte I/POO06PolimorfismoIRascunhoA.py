
# DEFINIÇÃO DE POLIMORFISMO

# Recaptulando, os 4 pilares da POO estudados no curso são abstração, encapsulamento, # herança e 
# polimorfismo.

# Ao contrário de outras linguagens de programação, em Python o polimorfismo não é dependente da herança.

# A palavra polimorfismo deriva do grego Polýs (vários) Morphé (forma), e a definição nos livros de POO 
# é 'propriedade ou estado daquilo que se apresenta e/ou se composta de várias formas diferentes'.

# O professor resumiu como 'um único nome, com comportamentos diferentes'.

# O exemplo usado em aula foi o do pato. Dependendo de onde ele está, sua locomoção será ou voar, ou nadar,
# ou andar. Portanto:

# Pato.locomover(meio)
# 
# Vai depender do terreno. Mesmo objeto (nome), diferentes comportamentos (locomover), neste caso 
# condicionados ao meio. Na água ele nada, no ar ele voa, e na terra ele anda.

# Mesmo nome, meios diferentes:

# Pato.locomover('terra')
# Pato.locomover('agua')
# Pato.locomover('ar')

# O mesmo nome do método, mas a depender do parâmetro, comandos diferentes.

# Exemplos simples de polimorfismo na linguagem Python associados a function overload e operator overload:

# Funcion Overload para a função len(): mesma função, vários resultados a depender dos parâmetros

# len('Rodrigo') retorna 7 (sete letras na palavra)
# len(['Sandy', 'Junior']) retorna 2 (2 itens na lista)
# len({'a':'x', 'b':'y'}) retorna 2 (2 itens chaveados no dicionário)

# Operator Overload para o sinal de '+': mesmo sinal, vários resultados a depender dos parâmetros

# + 5 é um número positivo
# 5 + 4 retorna 9 (a soma dos números)
# 'Poli' + 'Morfo' retorna PoliMorfo (contatenação dos 2 trechos)
# [3, 5] + [2, 4] retorna [3, 5, 2, 4] (junção de 2 listas)



# TIPOS DE POLIMORFISMO

# - Override
# - Overload
# - Coerção
# - Paramétrico



# OVERRIDE e OVERLOAD

# O Python suporta apenas 2 tipos de polimorfismo: override e overload

# OVERRIDE ou Subtyping é o Polimorfismo de INCLUSÃO, quando um método sobrescreve o método da mãe.
# Os métodos das SUBCLASSES criam ESPECIALIZAÇÕES dos métodos da SUPERCLASSE.

# No POOPolimorfismoRascunhoC dessa aula temos a SUPERCLASSE 'Animais' onde incluímos as SUBCLASSES 'Cachorro', 'Gato', 
# 'Pato' e 'Galinha'. Adicionalmente, adicionamos as raças de cachorro 'Spitz' e 'PibBull' herdando de 
# 'Cachorro'. Quanto mais abaixo na hierarquia, mais prevalente o método de mesmo nome (no caso o método
# 'emitir_som()'), portanto o método 'emitir_som()' da SUBCLASSE 'Spitz' sobrescreve (override) tanto o 
# método 'emitir_som()' da SUBCLASSE 'Cachorro', quanto o da SUPERCLASSE 'Animais'.

# No POOPolimorfismoRascunhod dessa aula temos a SUPERCLASSE 'Mae' onde incluímos as SUBCLASSES 'Filha'
# e 'Filho'. Apesar de a mãe possuir métodos de fazer pudim e fritar coxinha, a filha se especializou 
# (sobrescreveu) em pudim, e o filho se especializou (sobrescreveu) em coxinha.



# OVERLOAD é o Polimorfismo ad-hoc (para a finalidade) de SOBRECARGA, que será vista com mais profundiade
# na próxima aula.




# DUCK TYPING

# É um tipo de método polimórfico que utiliza funções polimórficas.






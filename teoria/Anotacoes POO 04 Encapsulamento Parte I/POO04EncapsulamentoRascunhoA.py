# ENCAPSULAMENTO

# Encapsulamento é um dos pilares da POO, o qual visa manter a integridade do sistema,
# protegendo o estado interno do objeto contra inteferência externa não regulamentada.

# Por exemplo, imaginando um botão que dispare um foguete intercontinental: somente uma
# pessoa autorizada pode apertar o botão, mas nem por isso ela quer saber tudo o que
# acontece depois que ela o aperta.

# Um dos principais objetivos do encapsulamento é proteger o sistema dos usuários que estão
# autorizados a usá-lo, limitando o acesso às partes que ela não deve acessar. No exemplo
# do botão, a pessoa tem acesso a ele, e o comando será executado se ela tiver autorização
# para isso.

# No exemplo do controle remoto dado na aula anterior sobre abstração, para proteger os
# circuitos e as placas, há uma cápsula onde apenas os botões estão acessíveis, caso
# contrário o contato com essas partes sensíveis poderia causar curto-circuito e perda do
# dispositivo.

# Na programação, o que fica exposto e disponível para o usuário em geral é chamado de
# INTERFACE PÚBLICA, e todos o resto fica ENCAPSULADO.

# Numa cápsula de suplemento por exemplo, a membrana exterior isola a dose exata dos
# compostos, impede a ação de fatores externos como umidade e luz, e protege o consumidor
# do gosto amargo e da eventual toxicidade direta no momento da ingestão.

# Vantagens do ENCAPSULAMENTO na computação são segurança e controle, facilidade de
# manutenção, flexibilidade e reutilização, e redução de efeitos colaterais.

# Para garantir a proteção necessária do código em qualquer linguagem de programação
# orientada a objeto, preciso entender dois conceitos-chave:

# - Visibilidade de atributos
# - Acesso aos dados protegidos



# VISIBILIDADE DE ATRIBUTOS

# Existem 3 tipos de visibilidade para atributos em linguagens de programação orientadas a
# objeto:

# - Pública (public: representada na teoria da POO pelo sinal de '+')
# - Protegida (protected: representada na teoria da POO pelo sinal de '#')
# - Privada (private: representada na teoria da POO pelo sinal de '-')

# Na visibilidade PÚBLICA, o atributo fica disponível para a SUPERCLASSE, AS SUBCLASSES, e
# todos o restante do programa, ou seja, é um atributo global plenamente acessível. Trata-se
# do escopo mais amplo de um atributo.

# Na visibilidade PROTEGIDA, o atributo fica disponível somente para a SUPERCLASSE e para
# as SUBCLASSES, ou seja, posso mexer no atributo através das classes, mas não posso mexer
# nele através do programa principal. Trata-se do escopo equilibrado de um atributo.

# Na visibilidade PRIVADA, o atributo fica disponível somente na CLASSE em que foi
# sinalizado (seja SUPER, seja SUB, desde que tenha sido designado individualmente em cada
# uma delas. Por exemplo, caso um atributo privado esteja definido numa SUPERCLASSE, nem as
# SUBCLASSES poderão mexer com ele, muito menos o programa principal. Trata-se do escopo
# mais restrito de um atributo.

# Porém, o Python não leva nenhum desses conceitos em conta. É possível proteger o código
# no Python, porém o escopo de visibilidade será sempre PÚBLICO. No Python, esse trabalho é
# feito através da convenção CONSENTING ADULTS: liberdade com responsabilidade (ideia por
# trás do 'adultos consentindo').

# 'Ao invés de criar barreiras concretas de modificadores de acesso, os desenvolvedores
# devem preferir estabelecer uma série de convenções que indicam como o acesso a esses
# elementos deve ser realizado.'

# No Python, a convenção das visualizações é a seguinte:

# PÚBLICA: atributo (só o atributo, sem prefixo nenhum, ao invés de '+')
# PROTEGIDA: _atributo (sufixo '_' ao invés de '#')
# PRIVADA: __atributo (sufixo '__' ao invés de '-')


# NAME MANGLING

# Name mangling é justamente a nomenclatura usada no Python para atributos PRIVADOS
# ('__' ou dois underlines antes do atributo). De fato ele foi criado para evitar as
# inconsistências de nome, mas é usado também (por convenção) para tornar determinados
# atributos privados.


# MÓDULOS e PACOTES são temas relacionados a funções, associados à reutilização de códigos
# em outros projetos. O agrupamento de vários módulos gera pacotes, os quais ampliam ainda
# mais a capacidade de modularização nos grandes projetos em Python.

# M O D U L A R I Z A Ç Ã O

# Útil quando os programas começam a tomar proporções muito grandes. Além de temerário, é
# muito confuso manter um programa escrito num arquivo só, com todas as funções e detalhes
# que os diferentes módulos desse programa exigem para seu funcionamento.

# A principal função da modularização é dividir programas grandes em pedaços menores que são
# separados por assunto, aumentando sua legibilidade e facilitando a manutenção do sistema
# completo.

# O desenvolvimento prático da aula está em arquivos distintos contidos na pasta Aula22.

# Os arquivos numeros22.py e uteis22.py são a primeira ilustração acerca de como importar
# módulos criados por mim para dentro do código do programa, e do efeito redutor do programa
# principal.

# VANTAGENS DA MODULARIZAÇÃO

# Melhor organização do código dada a divisão da resolução de grandes problemas e fatias
# menores;

# Facilidade de manutenção do código, seja para correções, seja para melhorias, pois por
# exemplo caso eu queira refinar ainda mais detalhes do cálculo de uma determinada função,
# basta alterar um arquivo (o que a contém), e todos os programas que a chamam serão
# beneficiados de uma vez;

# Ocultação do código detalhado, já que o programa principal fará apenas chamadas para as
# funções que estão em outro arquivo;

# Reutilização em outros projetos, o que é bastante útil quando trabalhamos em escopos
# especializados, por exemplo, dentro de uma empresa;

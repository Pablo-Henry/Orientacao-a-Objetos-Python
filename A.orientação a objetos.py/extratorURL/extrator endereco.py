endereco = "Rua Barra funda, 15, Jardim Santa Tereza, São Paulo - SP, 06813-180"

import re

# de zero até nove e o hífen pode ou não aparecer
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)

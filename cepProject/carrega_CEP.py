import requests
import json
from endereco import Endereco

cep = input("Digite um cep: ")

r = requests.get(f"http://viacep.com.br/ws/{cep}/json/")

if r.status_code == requests.codes.ok:

    j = json.loads(r.text)

    print(f'''

    VOCÊ PESQUISOU:

    CEP: {j['cep']}
    LOGRADOURO: {j['logradouro']}
    COMPLEMENTO: {j['complemento']}
    BAIRRO: {j['bairro']}
    LOCALIDADE:{j['localidade']} 
    UF: {j['uf']}
    IBGE: {j['ibge']} 
    GIA: {j['gia']}
    DDD: {j['ddd']}
    SIAFI: {j['siafi']}
    ''')

    endereco = Endereco()
    endereco.cep = j['cep']
    endereco.logradouro = j['logradouro']
    endereco.complemento = j['complemento']
    endereco.bairro = j['bairro']
    endereco.localidade = j['localidade']
    endereco.uf = j['uf']
    endereco.ibge = j['ibge']
    endereco.gia = j['gia']
    endereco.ddd = j['ddd']
    endereco.siafi = j['siafi']
    endereco.salvar()
    print('O ENDEREÇO FOI SALVO COM SUCESSO')

else:
    print('CEP não encontrado')

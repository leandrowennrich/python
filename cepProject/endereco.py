import sqlite3


class Endereco(object):

    def __init__(self):
        self.cep = None
        self.logradouro = None
        self.complemento = None
        self.bairro = None
        self.localidade = None
        self.uf = None
        self.ibge = None
        self.gia = None
        self.ddd = None
        self.siafi = None

    def cria_tabela(self):
        conn = sqlite3.connect('endereco.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS endereco(
            cep text, logradouro text, complemento text, bairro text, localidade text, uf text, ibge text, gia text, ddd text, siafi text
        )
        
        ''')

        conn.commit()

    def salvar(self):
        self.cria_tabela()

        conn = sqlite3.connect("endereco.db")
        cursor = conn.cursor()
        print(self.complemento)
        cursor.execute(f'''
        INSERT INTO endereco VALUES("{self.cep}","{self.logradouro}","{self.complemento}","{self.bairro}","{self.localidade}","{self.uf}","{self.ibge}",
        "{self.gia}","{self.ddd}","{self.siafi}")
        ''')
        conn.commit()

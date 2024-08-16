from manage_sql import MYSQL

db = MYSQL(
    host='localhost',
    user='',
    database='users',
    password='!',
    port=3306
)
nomeTabela='users'
colunas=['name', 'username', 'email', 'senha']

db.criarTabela(
    nomeTabela='users',
    Colunas=['name', 'username', 'email', 'senha'],
    ColunasTipo=['VARCHAR(255)', 'VARCHAR(255)', 'VARCHAR(255)', 'VARCHAR(255)']
)

dados = db.verDados(
    nomeTabela=nomeTabela
)
print(dados)
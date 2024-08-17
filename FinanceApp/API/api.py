from fastapi import FastAPI
from manage_sql import MYSQL
from pydantic import BaseModel

app = FastAPI()

class Dados(BaseModel):
    name: str
    username: str
    email: str
    password: str

db = MYSQL(
    host='',
    user='',
    password='',
    database='',
    port=3306
)

nometabela = 'usuarios'
colunas = ['name', 'username', 'email', 'password']

@app.post('/newuser/')
def newuser(dados: Dados):
    db.inserirDados(
        nomeTabela=nometabela,
        colunas=colunas,
        dados=[dados.name, dados.username, dados.email, db.encriptarValor(dados.password)]
    )

    return {'Sucesso': f'Usuário {dados.name} inserido com sucesso'}

@app.get('/user/{username}&{password}')
def login(username:str, password: str):
    dados = db.verDados(
        nomeTabela=nometabela,
        conditions=f'username = "{username}" and password = "{password}"',
        colunas="id,name,username"
    )

    if len(dados) > 0:
        return {dados[0][0]: {'Nome': dados[0][0], 'Username': dados[0][1]}}
    
    else:
        return {'Erro': 'Nenhum usuário encontrado'}
#.txt
# Banco de dados
# SQLite

# S-Q-L
# Linguagem de Consulta Estruturada

# SELECT * FROM CLIENTES
# Nome,sobrenome,idade 

# ORM
# É uma ferramenta que esconde os comandos SQL, 
# é uma bliblioteca, 
# e diminui o tamanho do codigo.

#MEU_BANCO é igual a db que significa data base

# I/O
# I= input(entrada)
# O= output(saída)

#computação na nuvem

import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# criando meu banco de dados
MEU_BANCO=create_engine("sqlite:///meubanco.db")

#criando conexão com o banco de dados
Session=sessionmaker(bind=MEU_BANCO)
session=Session()

#criando tabela.
Base=declarative_base()

class Usuario(Base):
    __tablename__="usuarios"
    
    #definindo campos da tabela
    id=Column("id", Integer, primary_key=True, autoincrement=True)
    nome=Column("nome", String)
    email=Column("email", String)
    senha=Column("senha", String)
    
    #definindo atributos da tabela
    def __init__(self, nome:str, email:str, senha:str):
        self.nome= nome
        self.email= email
        self.senha=senha
#init na função é utilizado dentro desse class, 
#para que quando o código começar a rodar o class,
#essa função vos dara as caractéristicas.

#criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

#salvar no banco de dados.
os.system("cls || clear")

print("Solicitando dados para o usuário")
inserir_nome=input("Digite seu nome:")
inserir_email=input("Digite seu email:")
inserir_senha=input("Digite sua senha:")
     
usuario=Usuario(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(usuario)
session.commit()

#listando todos os usuários do banco de dados.
print("Exibindo todos os usuários do banco de dados.")
lista_usuarios=session.query(Usuario).all()

#Read
for usuario in lista_usuarios:
    print(f"{usuario.id}-{usuario.nome}-{usuario.email}-{usuario.senha}")

#Delete.
print("\nExcluindo um usuário")
email_usuario=input("Informe o email do usuario para ser excluido:")
usuario=session.query(Usuario).filter_by(email=email_usuario).first()
session.delete(usuario)
session.commit()
print("Usuário excluido com sucesso.")

#listando todos os usuários do banco de dados.
print("Exibindo todos os usuários do banco de dados.")
lista_usuarios=session.query(Usuario).all()

#Read
for usuario in lista_usuarios:
    print(f"{usuario.id}-{usuario.nome}-{usuario.email}-{usuario.senha}") 

#update 
print("\nAtualizando dados do usuário.")
usuario=session.query(Usuario).filter_by(email=email_usuario).first()

novos_dados=Usuario(
    nome=input("Digite seu nome"),
    email=input("Digite seu email"),
    senha=input("Digite seu senha")
)
usuario=novos_dados
session.add(usuario)
session.commit()
    
#fechando conexão.
session.close()


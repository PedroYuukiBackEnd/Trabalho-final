from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()


def cadastrar_produto(nome_produto, categoria_produto, preco_produto, quant_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome_produto, categoria_produto, preco_produto, quant_produto)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao cadastrar o Produto: {erro}")
        finally:
            cursor.close()
            conexao.close()


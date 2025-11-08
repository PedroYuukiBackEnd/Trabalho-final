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


def listar_produto():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY ID"
            )
            return cursor.fetchall()      
        except Exception as erro:
            print(f"Erro ao tentar exbir Produtos: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()

def atualizar_produto(id, novo_preco, nova_quantidade):
    conexao, cursor = conectar() 
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET preco = %s, quantidade = %s WHERE id = %s",
                (novo_preco, nova_quantidade, id)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print("Produto atualizado com sucesso!")
            else:
                print("Nenhum produto encontrado com esse ID.")
        except Exception as erro:
            print(f"Erro ao tentar atualizar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()
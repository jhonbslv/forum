from dao import conectar

def listar_posts():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()

    cursor.close()
    conn.close()
    return posts


def buscar_post(id):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cursor.fetchone()

    cursor.close()
    conn.close()
    return post


def inserir_post( id,titulo, resumo, conteudo, autor):
    conn = conectar()
    cursor = conn.cursor()

    query = """
    INSERT INTO posts (id,titulo, resumo, conteudo, autor)
    VALUES (%s,%s, %s, %s, %s)
    """

    cursor.execute(query, (id,titulo, resumo, conteudo, autor))
    conn.commit()

    cursor.close()
    conn.close()


def atualizar_post(id, titulo, resumo, conteudo, autor):
    conn = conectar()
    cursor = conn.cursor()

    query = """
    UPDATE posts
    SET titulo=%s, resumo=%s, conteudo=%s, autor=%s
    WHERE id=%s
    """

    cursor.execute(query, (titulo, resumo, conteudo, autor, id))
    conn.commit()

    cursor.close()
    conn.close()


def deletar_post(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM posts WHERE id = %s""", (id,))
    conn.commit()

    cursor.close()
    conn.close()
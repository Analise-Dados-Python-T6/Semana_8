import psycopg2

conexao = psycopg2.connect(
    host="localhost", port="5432", dbname=" ",
    user="postgres", password=" ")
cursor = conexao.cursor()
cursor.execute("SELECT version();")
print("Conectado!", cursor.fetchone()[0])

# Reaproveitando a mesma conexão para listar as tabelas do banco
cursor.execute(
    "SELECT table_name FROM information_schema.tables "
    "WHERE table_schema = 'public';"
)
tabelas = cursor.fetchall()
print("Tabelas encontradas:", tabelas)

conexao.close()

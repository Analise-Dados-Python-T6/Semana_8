import pyodbc

conexao = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"  # ajustar para a versão do driver instalada (ex: 18)
    "SERVER=localhost;PORT=1433;DATABASE= ;"  # ajustar SERVER e informar o nome do DATABASE
    "UID=sa;PWD= "  # ajustar UID (usuário) e informar a PWD (senha)
)
cursor = conexao.cursor()
cursor.execute("SELECT @@VERSION;")
print("Conectado!", cursor.fetchone()[0])

# Reaproveitando a mesma conexão para listar as tabelas do banco
cursor.execute(
    "SELECT table_name FROM information_schema.tables "
    "WHERE table_schema = 'dbo';"
)
tabelas = cursor.fetchall()
print("Tabelas encontradas:", tabelas)

conexao.close()

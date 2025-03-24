import sqlite3
import uuid

# Conectar ao banco
conn = sqlite3.connect(r'E:\BlueSky Project\ASE\sistemas\Emails_auto\data\emails_empresas copy.db')
cursor = conn.cursor()

# Selecionar todas as empresas
cursor.execute("SELECT id_empresa FROM token")
token = cursor.fetchall()

# Atualizar cada registro com um token único
for (id_empresa,) in token:
    token = str(uuid.uuid4())
    cursor.execute("UPDATE token SET token = ? WHERE id_empresa = ?", (token, id_empresa))

conn.commit()
conn.close()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3

# Configuração do e-mail
EMAIL_SENDER = "projectaurorasys@gmail.com"  # Seu e-mail
EMAIL_PASSWORD = "qwxi asqt mnsf xxai"  # Senha ou senha de app
SMTP_SERVER = "smtp.gmail.com"  # Servidor SMTP
SMTP_PORT = 587  # Porta do servidor SMTP

# Caminho para o banco de dados
DB_PATH = r"E:\BlueSky Project\ASE\sistemas\Emails_auto\data\emails_empresas.db"

# Função para enviar e-mail
def enviar_email(destinatario, empresa_name):
    # Criando o e-mail com HTML estilizado
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = destinatario
    msg["Subject"] = "Participe do nosso Diagnóstico de Transformação Digital🔎"
    msg.add_header("Reply-To", EMAIL_SENDER)  # Adiciona "Responder Para"
    
    # Lê o conteúdo HTML do arquivo
    with open("web\\email.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    
    # Substitui o nome da empresa no conteúdo HTML
    html_content = html_content.replace("[empresa_name]", empresa_name)
    msg.attach(MIMEText(html_content, "html"))

    # Configuração do servidor SMTP e envio do e-mail
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Segurança na conexão
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, destinatario, msg.as_string())
        server.quit()
        print(f"✅ E-mail enviado para: {destinatario}")
    except Exception as e:
        print(f"❌ Falha ao enviar e-mail para {destinatario}: {e}")

# Conectar ao banco de dados e buscar os e-mails
def buscar_emails():
    try:
        conn = sqlite3.connect(DB_PATH)  # Conectando ao banco de dados
        cursor = conn.cursor()
        cursor.execute("SELECT empresa_name, email FROM empresa_teste")  # Consulta os e-mails
        empresas = cursor.fetchall()
        
        for empresa in empresas:
            empresa_name, email = empresa
            enviar_email(email, empresa_name)  # Envia o e-mail para cada empresa
        
        conn.close()
    except sqlite3.Error as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")

# Iniciar o processo de envio de e-mails
buscar_emails()

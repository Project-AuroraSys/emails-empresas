import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os
from dotenv import load_dotenv  # Importa a biblioteca dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do e-mail (lendo do .env)
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

# Lista de contatos
contatos = [ 
    ("Nome", "@gmail.com")
]

# Função para enviar e-mail
def enviar_email(destinatario, empresa_name):
    msg = MIMEMultipart("alternative")  # Define o tipo de e-mail
    msg["From"] = EMAIL_SENDER
    msg["To"] = destinatario
    msg["Subject"] = "Participe do nosso levantamento exclusivo 🔎"
    
    # Cabeçalhos para melhor entrega
    msg.add_header("Reply-To", "support@aurorasystementerprise.com")
    msg.add_header("List-Unsubscribe", "<mailto:unsubscribe@aurorasystementerprise.com>, <https://aurorasystementerprise.com/unsubscribe>")

    # Versão plaintext do e-mail (simples, sem HTML)
    plain_text = f"""
    Olá {empresa_name},

    Queremos convidá-lo para um levantamento exclusivo sobre Transformação Digital promovido pela Aurora Systems Enterprise.

    Nosso questionário abrange temas como:
    - Infraestrutura e tecnologias utilizadas
    - Automação e ferramentas digitais
    - Capacitação da equipe para o digital
    - Desafios e oportunidades na digitalização

    Sua opinião é essencial! Para participar, acesse o formulario abaixo:
    https://docs.google.com/forms/d/e/1FAIpQLSds5U31gndXAuRi-asP1ufj8zdLA4uajc609wI0OnY7oyshGQ/viewform?usp=header

    Contamos com sua participação! 😊

    Atenciosamente,
    Equipe de Pesquisa Aurora Systems Enterprise
    """

    # Lê o conteúdo HTML do arquivo
    with open("web/email2.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    # Personaliza o e-mail com o nome da empresa
    html_content = html_content.replace("[empresa_name]", empresa_name)

    # Adiciona ambas as versões ao e-mail
    msg.attach(MIMEText(plain_text, "plain"))  # Adiciona o texto puro primeiro
    msg.attach(MIMEText(html_content, "html"))  # Depois adiciona o HTML (prioridade)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, destinatario, msg.as_string())
        server.quit()
        print(f"✅ E-mail enviado para: {destinatario}")
    except Exception as e:
        print(f"❌ Falha ao enviar e-mail para {destinatario}: {e}")

# Enviar e-mails para os contatos
def enviar_emails_contatos():
    for nome, email in contatos:
        enviar_email(email, nome)
        time.sleep(5)  # Evita bloqueios por envio rápido

# Iniciar envio
enviar_emails_contatos()

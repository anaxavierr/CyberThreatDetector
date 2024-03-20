import boto3

# Configurações do AWS SQS
queue_url = 'https://sqs.us-east-1.amazonaws.com/058264345289/fila-firewall-ids-ips'  # URL da fila do SQS para logs de firewall e IDS/IPS

# Função para enviar dados para o SQS
def publish_to_sqs(logs, queue_url, profile_name):
    session = boto3.Session(profile_name=profile_name)
    sqs = session.client('sqs', region_name='us-east-1')
    
    for log in logs:
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=log
        )
        print(f'Mensagem publicada: {response["MessageId"]}')

# Leitura dos arquivos de logs
with open('/workspaces/CyberThreatDetector/data/firewall_logs.txt', 'r') as file:
    firewall_logs = file.readlines()

with open('/workspaces/CyberThreatDetector/data/ids_ips_logs.txt', 'r') as file:
    ids_ips_logs = file.readlines()

# Nome do perfil AWS CLI
profile_name = 'aws-data'

# Envio dos dados para o SQS.
publish_to_sqs(firewall_logs, queue_url, profile_name)
publish_to_sqs(ids_ips_logs, queue_url, profile_name)

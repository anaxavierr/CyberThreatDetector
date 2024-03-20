from google.cloud import pubsub_v1

# Configurações do Google Cloud Pub/Sub
project_id = 'seu-projeto-id'
topic_name = 'topic-firewall-ips-logs'  # Nome do tópico Pub/Sub para logs de firewall e IDS/IPS

# Função para enviar dados para o Pub/Sub
def publish_to_pubsub(logs, topic_name):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)
    
    for log in logs:
        future = publisher.publish(topic_path, log.encode('utf-8'))
        print(f'Mensagem publicada: {future.result()}')

# Leitura dos arquivos de logs
with open('firewall_logs.txt', 'r') as file:
    firewall_logs = file.readlines()

with open('ids_ips_logs.txt', 'r') as file:
    ids_ips_logs = file.readlines()

# Envio dos dados para o Pub/Sub
publish_to_pubsub(firewall_logs, 'topic-firewall-logs')
publish_to_pubsub(ids_ips_logs, 'topic-ids-ips-logs')

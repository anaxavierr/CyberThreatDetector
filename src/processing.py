import boto3

# Configurações do AWS SQS
queue_url = 'https://sqs.us-east-1.amazonaws.com/058264345289/fila-firewall-ids-ips'  # URL da fila do SQS para logs de firewall e IDS/IPS

# Função para processar mensagens do SQS
def process_sqs_messages(message):
    # Processamento dos dados (exemplo: análise de padrões, detecção de ameaças, etc.)
    processed_data = message['Body'].upper()  # Exemplo simples: converter os dados para maiúsculas
    
    # Salvar os dados processados em um local adequado (exemplo: Amazon S3)
    # Inserir código para salvar os dados em um bucket do Amazon S3
    
    print(f'Dados processados: {processed_data}')
    
    # Deletar a mensagem da fila após o processamento
    receipt_handle = message['ReceiptHandle']
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )

# Função para consumir mensagens do SQS
def consume_sqs_messages(queue_url):
    sqs = boto3.client('sqs')
    
    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=20
        )
        
        if 'Messages' in response:
            for message in response['Messages']:
                process_sqs_messages(message)
        else:
            print('Nenhuma mensagem disponível na fila.')

# Consumir mensagens do SQS
consume_sqs_messages(queue_url)

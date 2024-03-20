# -*- coding: utf-8 -*-
import random
import datetime

# Função para gerar logs de firewall
def generate_firewall_logs(num_logs):
    logs = []
    for _ in range(num_logs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
        destination_ip = f"10.0.{random.randint(0, 255)}.{random.randint(0, 255)}"
        action = random.choice(["ALLOW", "DENY"])
        log_entry = f"{timestamp} | {source_ip} -> {destination_ip} | {action}"
        logs.append(log_entry)
    return logs

# Função para gerar logs de IDS/IPS
def generate_ids_ips_logs(num_logs):
    logs = []
    for _ in range(num_logs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
        destination_ip = f"10.0.{random.randint(0, 255)}.{random.randint(0, 255)}"
        threat_type = random.choice(["SQL Injection", "Cross-Site Scripting", "Malware", "Brute Force"])
        log_entry = f"{timestamp} | {source_ip} -> {destination_ip} | {threat_type}"
        logs.append(log_entry)
    return logs

# Função para salvar logs em um arquivo
def save_logs_to_file(logs, filename):
    with open(filename, 'w') as file:
        for log in logs:
            file.write(log + '\n')

# Número de logs a serem gerados
num_logs = 1000

# Gerar logs de firewall
firewall_logs = generate_firewall_logs(num_logs)
save_logs_to_file(firewall_logs, 'firewall_logs.txt')

# Gerar logs de IDS/IPS
ids_ips_logs = generate_ids_ips_logs(num_logs)
save_logs_to_file(ids_ips_logs, 'ids_ips_logs.txt')

print("Logs gerados com sucesso!")

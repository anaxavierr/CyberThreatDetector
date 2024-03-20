# Sistema de Detecção de Ameaças de Segurança Cibernética

## Visão Geral do Projeto
Este projeto consiste em um sistema de detecção de ameaças de segurança cibernética que utiliza dados de logs de firewalls e IDS/IPS para identificar e responder proativamente a ameaças de phishing por mensagens instantâneas e acesso de contas comprometidas em tempo real.

## Instruções de Configuração
1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter instalado o Python e as bibliotecas necessárias listadas no arquivo requirements.txt.
3. Configure suas credenciais do Google Cloud Platform (GCP) para acessar os serviços necessários.
4. Substitua os placeholders 'seu-projeto-id', 'topic-firewall-logs', 'topic-ids-ips-logs' e 'subscription-firewall-ips-logs' pelas informações corretas do GCP no código fonte.

## Guia de Instalação e Uso
1. Execute o script de geração de dados fictícios para criar logs de firewall e IDS/IPS.
2. Execute o script de ingestão de dados para enviar os logs gerados para o Google Cloud Pub/Sub.
3. Execute o script de processamento de dados para processar as mensagens do Pub/Sub e armazenar os dados processados.

## Dados Fictícios
Os dados fictícios de logs de firewall e IDS/IPS são gerados aleatoriamente por meio de scripts Python incluídos neste repositório. Eles são usados para simular o comportamento de logs reais de segurança cibernética.

## Modelos de Detecção de Ameaças
Os modelos de detecção de ameaças incluídos neste projeto são exemplos simples para fins de demonstração. Eles podem ser substituídos ou aprimorados conforme necessário para atender às necessidades específicas de detecção de ameaças da sua organização.

## Contribuição e Feedback
Se você deseja contribuir com melhorias para este projeto ou fornecer feedback, fique à vontade para abrir uma issue ou enviar uma solicitação de recebimento (pull request).

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

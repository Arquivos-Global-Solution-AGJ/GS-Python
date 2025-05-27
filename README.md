
# 🌧️ SOS ENCHENTES - Sistema de Apoio em Desastres Naturais

## Descrição do Projeto

O **SOS ENCHENTES** é um sistema simples desenvolvido em Python que visa ajudar pessoas durante eventos extremos, como chuvas intensas e enchentes. Ele oferece informações sobre riscos de alagamento em bairros, dicas de segurança, alertas meteorológicos simulados e permite que os usuários relatem problemas em suas regiões, contribuindo para um **mapeamento colaborativo** das áreas afetadas.

## Funcionalidades

- ✅ **Verificar risco de inundação na sua área**
- ✅ **Receber dicas de proteção antes, durante e após enchentes**
- ✅ **Consultar situação atual (alerta antecipado com simulação de previsão)**
- ✅ **Relatar problemas (alagamentos, deslizamentos, enxurradas) para ajudar outros usuários**
- ✅ **Acesso rápido a contatos de emergência**
- ✅ **Sistema de dados colaborativos dos usuários**

## Tecnologias Utilizadas

- 🔹 **Python 3**
- 🔹 Bibliotecas: `random`, `time`

## Como Funciona?

O sistema possui um menu interativo onde o usuário escolhe uma das opções:

1. 🔍 **Verificar risco de inundação:**  
   O usuário informa seu bairro, e o sistema verifica se consta em uma base de dados com níveis de risco (`baixo`, `médio`, `alto`). Caso não esteja, verifica se há relatos colaborativos recentes.

2. 🛡️ **Dicas de proteção:**  
   Apresenta orientações importantes antes, durante e depois de uma enchente.

3. 📡 **Situação atual:**  
   Simula uma previsão com base em risco aleatório: `baixo`, `moderado` ou `alto`. Mostra mensagens e alertas conforme o risco.

4. 🗺️ **Relatar problema:**  
   Usuário pode reportar situações como alagamento, deslizamento ou enxurrada em seu bairro, contribuindo para um **mapeamento colaborativo** de áreas afetadas.

5. ☎️ **Contatos de emergência:**  
   Lista telefones de serviços importantes como Defesa Civil, Bombeiros, SAMU e Polícia Militar, além de orientações de como pedir ajuda.

6. 🚪 **Sair:**  
   Finaliza o programa.

## 🚀 Como Executar

1. Instale o Python (versão 3 ou superior) no seu computador.
2. Copie o código para um arquivo chamado, por exemplo, `sos_enchentes.py`.
3. No terminal, navegue até a pasta onde está salvo e execute:

```bash
python sos_enchentes.py
```

## 🔥 Exemplos de Uso

- Verificar se o bairro "Campo Limpo" está em risco de enchente.
- Receber orientações sobre como se proteger em caso de alagamentos.
- Consultar uma previsão simulada da situação atual.
- Reportar que há um "alagamento" no bairro "Mooca", contribuindo para o alerta da comunidade.

## 💡 Ideias de Evolução

- 🔗 Integração com APIs meteorológicas em tempo real.
- 🌍 Implementar um mapa visual com dados colaborativos.
- 📲 Transformar em um aplicativo mobile para Android/iOS.
- 🔔 Envio de notificações automáticas para usuários em áreas de risco.

## 🆘 Contatos de Emergência

- Defesa Civil: 199  
- Bombeiros: 193  
- Polícia Militar: 190  
- SAMU (ambulância): 192  

## 🤝 Contribuição

Contribuições são bem-vindas! Você pode melhorar o sistema, corrigir bugs ou propor novas funcionalidades.

## 📜 Licença

Este projeto é de código aberto e livre para uso educativo e não comercial.

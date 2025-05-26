import random
import time

# Base de dados simulada de bairros em risco
bairros_de_risco = {
    'chácara santo antônio': 'risco alto',
    'bosque da saúde': 'risco médio',
    'campo limpo': 'risco alto',
    'capela do socorro': 'risco alto',
    'm\'boi mirim': 'risco alto',
    'santo amaro': 'risco médio',
    'parelheiros': 'risco alto',
    'jardim emburá': 'risco alto',
    'itaquera': 'risco médio',
    'aricanduva': 'risco médio',
    'jardim romano': 'risco alto',
    'freguesia do ó': 'risco médio',
    'pirituba': 'risco médio',
    'butantã': 'risco baixo',
    'lapa': 'risco baixo',
    'sé': 'risco baixo'
}

# Dados colaborativos dos usuários
bairros_colaborativos = {}

def menu_principal():
    print("\n---🌧️ SOS ENCHENTES - Sistema de Apoio em Desastres Naturais 🌧️---")
    print("1️⃣ - Verificar risco de inundação na sua área")
    print("2️⃣ - Dicas de proteção e segurança")
    print("3️⃣ - Consultar situação atual (alerta antecipado)")
    print("4️⃣ - Relatar problema na sua região (mapeamento colaborativo)")
    print("5️⃣ - Contatos de emergência")
    print("6️⃣ - Sair")
    print("------------------------------------------------------------")

def escolha_menu():
    try:
        escolha = int(input("Escolha uma opção (1 a 6): "))
        return escolha
    except ValueError:
        print("⚠️ Digite apenas números.")
        return None

def minha_area():
    bairro = input("Digite seu bairro: ").strip().lower()

    if bairro in bairros_de_risco:
        print(f"\n⚠️ ALERTA: Sua área ({bairro.title()}) tem {bairros_de_risco[bairro]} risco de alagamento!\n")
    elif bairro in bairros_colaborativos:
        print(f"\n🔎 ⚠️ Alerta colaborativo: Usuários reportaram {bairros_colaborativos[bairro]} na sua região.\n")
    else:
        print("\n✅ Sua área não consta como de risco elevado no momento, mas continue atento às previsões e alertas.\n")

def me_proteger():
    print("""
🛡️  Dicas de Proteção e Segurança:

ANTES DA INUNDAÇÃO:
✅ Monitore alertas meteorológicos.
✅ Tenha um plano de evacuação.
✅ Monte um kit de emergência.
✅ Desligue energia elétrica e gás se necessário.
✅ Proteja seus móveis com suportes elevados.

DURANTE A INUNDAÇÃO:
🚨 Siga as orientações da Defesa Civil (199) e Bombeiros (193).
🚫 Nunca tente atravessar áreas alagadas, nem a pé nem de carro.
🆘 Vá para lugares altos.

DEPOIS DA INUNDAÇÃO:
🔧 Limpe e desinfete seu imóvel.
📜 Documente os danos para seguro ou ajuda governamental.
🩺 Verifique riscos sanitários (água contaminada).
""")

def situacao_atual():
    risco = random.choice(['baixo', 'moderado', 'alto'])
    print("\n📡 Analisando dados meteorológicos...")
    time.sleep(2)

    if risco == "alto":
        print("\n🚨 ALERTA VERMELHO: Chuvas intensas nas próximas horas. Alto risco de enchentes. Aja com cautela!")
    elif risco == "moderado":
        print("\n⚠️ ALERTA AMARELO: Chuva moderada prevista. Atenção a possíveis pontos de alagamento.")
    else:
        print("\n☀️ Céu limpo! Sem risco de alagamentos nas próximas horas. Aproveite com responsabilidade.")

def relatar_problema():
    bairro = input("Digite o nome do bairro onde há problemas: ").strip().lower()
    problema = input("Descreva brevemente o problema (ex: 'alagamento', 'deslizamento', 'enxurrada'): ").strip().lower()

    bairros_colaborativos[bairro] = problema
    print(f"\n📍 Obrigado! Seu relato sobre '{problema}' no bairro '{bairro.title()}' foi registrado e ajudará outras pessoas.\n")

def contatos():
    print("""
📞 CONTATOS DE EMERGÊNCIA:
- Defesa Civil: 199
- Corpo de Bombeiros: 193
- Polícia Militar: 190
- SAMU (ambulância): 192

📝 Ao ligar:
- Fique calmo(a).
- Informe seu nome e telefone.
- Descreva claramente o problema e a localização exata.
- Diga se há vítimas e quantas.
- Forneça pontos de referência.
""")

def main():
    while True:
        menu_principal()
        opcao = escolha_menu()

        if opcao == 1:
            minha_area()
        elif opcao == 2:
            me_proteger()
        elif opcao == 3:
            situacao_atual()
        elif opcao == 4:
            relatar_problema()
        elif opcao == 5:
            contatos()
        elif opcao == 6:
            print("\n👋 Obrigado por usar o SOS ENCHENTES. Fique seguro(a) e atento(a)!")
            break
        else:
            print("❌ Opção inválida. Digite um número de 1 a 6.")

main()

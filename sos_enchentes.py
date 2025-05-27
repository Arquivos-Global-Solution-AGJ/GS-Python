def menu_principal():
    while True:
        print("---Bem vindo(a) ao sistema do SOS ENCHENTES---")
        print("(1) Minha área corre risco de inundar? \n(2) Como posso me proteger de possíveis inundações? \n(3) Agora está perigoso? \n(4) Precisa de ajuda? contate-nos IMEDIATAMENTE \n(5) Sair")
        escolha = int(input())
        if escolha == 1:
            minha_area()
        elif escolha == 2:
            me_proteger()
        elif escolha == 3:
            situacao_atual()
        elif escolha == 4:
            contatos()
        else:
            menu_principal()


##função minha_area
def minha_area():
    print("Inicialmente voltado para a cidade de São Paulo!")
    bairro = input("\nDigite seu bairro: ").strip().lower()
    bairros_de_risco = ['chácara santo antônio', 'bosque da saúde', 'campo limpo', 'capela do socorro','m\'boi mirim', 'santo amaro', 'parelheiros', 'jardim emburá','itaquera', 'aricanduva', 'vila formosa', 'penha', 'mooca', 'jardim romano','vila maria', 'vila guilherme', 'santana', 'tucuruvi', 'jaçanã', 'tremembé','freguesia do ó', 'pirituba', 'jaraguá', 'jardim guançã','butantã', 'lapa', 'pinheiros', 'sé']
    if bairro in bairros_de_risco:
        print("⚠️ Cuidado! Essa área é considera de fácil alagamento\n\n")
    else:
        print("Essa área não é considerada de fácil alagamento, mas pode ocorrer, fique atento!\n\n")

##Função me_proteger
def me_proteger():
    print("Se você escolheu essa opção. Fique atento as instruções \n ANTES DA INUNDAÇÃO \n1º Monitore alertas meteorológicos\n2º Tenha um plano de evacuação – Saiba quais rotas usar e onde estão os abrigos mais próximos.\n3º Monte um kit de emergência – Inclua água potável, alimentos não perecíveis, lanternas, pilhas, rádio, documentos importantes, remédios, roupas extras e itens de higiene.\n4º Desconecte aparelhos elétricos – Evite riscos de curtos-circuitos ou choques.\n5º Avalie a estrutura da sua casa – Se for uma área de risco, considere sair antes do alagamento.\n\n ⚠️DURANTE A INUNDAÇÃO⚠️\n -Mantenha a calma e acione a Defesa Civil (199) ou Corpo de Bombeiros (193).\n -Saia do local se as autoridades pedirem.\n -Nunca tente atravessar áreas alagadas a pé ou de carro. \n\n DEPOIS DA INUNDAÇÃO \n -Espere autorização das autoridades para retornar ao imóvel.\n -Evite contato com a água residual.\nAtualize seus documentos e registre os danos, caso precise de apoio do governo ou seguro.\n\n Essas instruções são conferidas por especialistas, proteja-se, a natureza não brinca!")

##função situacao_atual
def situacao_atual():
    import random 
    risco = random.choice(['baixo', 'moderado' , 'alto'])
    if risco == "alto":
        print("\n 🚨 Alerta! Chuva forte nas próximas horas com risco de alagamento, fique atento(a)!")
    elif risco == "moderado"
        print("\n⚠️ Atenção: Chuva moderada prevista nas próximas horas, fique atento(a)!")
    else:
        print("\n☀️ Sem chuva prevista para as próximas horas, aproveite o dia!")

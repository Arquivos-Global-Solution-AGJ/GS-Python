def menu_principal():
    while True:

        print("(1) Minha área corre risco de inundar? \n(2) Como posso me protejer de possíveis inundações? \n(3) Agora está perigoso? \n(4) Precisa de ajuda? contate-nos IMEDIATAMENTE \n (5) Sair")
        escolha = int(input())
        if escolha == 1:
            minha_area()
        elif escolha == 2:
            me_protejer()
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
    bairros_de_risco = ['chácara santo antônio', 'bosque da saúde', 'campo limpo', 'capela do socorro','m\'boi mirim', 'santo amaro', 'parelheiros', 'jardim emburá',
    'itaquera', 'aricanduva', 'vila formosa', 'penha', 'mooca', 'jardim romano','vila maria', 'vila guilherme', 'santana', 'tucuruvi', 'jaçanã', 'tremembé','freguesia do ó', 'pirituba', 'jaraguá', 'jardim guançã',
    'butantã', 'lapa', 'pinheiros', 'sé']
    if bairro in bairros_de_risco:
        print("⚠️ Cuidado! Essa área é considera de fácil alagamento")
    else:
        print("Essa área não é considerada de fácil alagamento, mas pode ocorrer, fique atento!")
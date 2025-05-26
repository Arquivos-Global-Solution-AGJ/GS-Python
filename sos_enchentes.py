def menu_principal():
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


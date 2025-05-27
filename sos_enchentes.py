def menu_principal():
    print("---Bem vindo(a) ao sistema do SOS ENCHENTES---\n")
    print("(1) Minha área corre risco de inundar? \n(2) Como posso me proteger de possíveis inundações? \n(3) Agora está perigoso? \n(4) Precisa de ajuda? contate-nos IMEDIATAMENTE \n(5) Sair")
        
        
def escolha_menu():       
    while True:
        escolha = int(input())
        if escolha == 1:
            minha_area()
        elif escolha == 2:
            me_proteger()
        elif escolha == 3:
            situacao_atual()
        elif escolha == 4:
            contatos()
        elif escolha == 5:
            print("Obrigado por usar o SOS enchentes.")
            break
            return escolha
        else:
            print("Opção inexistente, digite de 1 a 5.")

##função minha_area
def minha_area():
    print("Inicialmente voltado para a cidade de São Paulo!")
    bairro = input("\nDigite seu bairro: ").strip().lower()
    bairros_de_risco = ['chácara santo antônio', 'bosque da saúde', 'campo limpo', 'capela do socorro','m\'boi mirim', 'santo amaro', 'parelheiros', 'jardim emburá','itaquera', 'aricanduva', 'vila formosa', 'penha', 'mooca', 'jardim romano','vila maria', 'vila guilherme', 'santana', 'tucuruvi', 'jaçanã', 'tremembé','freguesia do ó', 'pirituba', 'jaraguá', 'jardim guançã','butantã', 'lapa', 'pinheiros', 'sé']
    if bairro in bairros_de_risco:
        print("\n⚠️ -Cuidado! Essa área é considera de fácil alagamento\n\n")
    else:
        print("\nEssa área não é considerada de fácil alagamento, mas pode ocorrer, fique atento!\n\n")
    menu_principal()

##Função me_proteger
def me_proteger():
    print("\n\nSe você escolheu essa opção. Fique atento as instruções \n\n ANTES DA INUNDAÇÃO: \n -Monitore alertas meteorológicos\n -Tenha um plano de evacuação – Saiba quais rotas usar e onde estão os abrigos mais próximos.\n -Monte um kit de emergência – Inclua água potável, alimentos não perecíveis, lanternas, pilhas, rádio, documentos importantes, remédios, roupas extras e itens de higiene.\n -Desconecte aparelhos elétricos – Evite riscos de curtos-circuitos ou choques.\n -Avalie a estrutura da sua casa – Se for uma área de risco, considere sair antes do alagamento.\n\n ⚠️--DURANTE A INUNDAÇÃO--⚠️:\n -Mantenha a calma e acione a Defesa Civil (199) ou Corpo de Bombeiros (193).\n -Saia do local se as autoridades pedirem.\n -Nunca tente atravessar áreas alagadas a pé ou de carro. \n\n DEPOIS DA INUNDAÇÃO: \n -Espere autorização das autoridades para retornar ao imóvel.\n -Evite contato com a água residual.\n -Atualize seus documentos e registre os danos, caso precise de apoio do governo ou seguro.\n\n Essas instruções são conferidas por especialistas, proteja-se, a natureza não brinca!\n\n")
    menu_principal()

##função situacao_atual
def situacao_atual():
    import random 
    risco = random.choice(['baixo', 'moderado' , 'alto'])
    if risco == "alto":
        print("\n 🚨 -Alerta! Chuva forte nas próximas horas com risco de alagamento, fique atento(a)!\n\n")
    elif risco == "moderado":
        print("\n⚠️ -Atenção: Chuva moderada prevista nas próximas horas, fique atento(a)!\n\n")
    else:
        print("\n☀️ -Sem chuva prevista para as próximas horas, aproveite o dia!\n\n")
    menu_principal()

##função contatos
def contatos():
    print("---CONTATOS QUE VOCÊ PODE LIGAR NA EMERGÊNCIA---\n\n Defesa Civil – 199 \n Polícia Militar – 190 \n Bombeiros – 193 \n SAMU – 192\n\n Ao telefonar:\n -Fique calmo\n -Identifique-se fornecendo o nome e o telefone de contato\n -Diga exatamente o que está acontecendo\n -Informe se há vítimas. Havendo, forneça precisamente o número de pessoas\n -Forneça corretamente o endereço e, se possível, uma ou mais referências\n\n")
    menu_principal()

##função main
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
            contatos()
        else:
            break
            
main()
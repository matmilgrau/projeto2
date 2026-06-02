
import random
import time

def termo():
    txt = ["apoio", "letra", "sagaz", "mexer", "amigo", "banco", "carro", "dente", 
    "festa", "hotel", "ideia", "livro",
    "noite", "porta", "radio", "sabor", "tempo", "vento", "zebra", "ajuda",
    "baixo", "corpo", "desde", "exame", "falar", "geral", "haver",
    "justo", "aluno", "astro", "beijo", "bravo", "campo", "chave", "chuva", "claro", 
    "creme", "disco", "doado", "duelo", "exato", "fundo", "grito", "globo", "humor", 
    "jovem", "largo", "lente", "limpo", "marco", "metro", "mundo", "navio", 
    "nuvem", "ontem", "ordem", "pauta", "pedra", "piano", "ponto", "quase", "abril", 
    "agora", "andar", "antes", "arena", "autor", "aviso", "balão", "bater", "beira", 
    "bloco", "bolsa", "borda", "brisa", "busca", "calor", "causa", "cesta", "clima", 
    "coisa", "conta", "crime", "curto", "dança", "drama", "duplo", "etapa", "fator",
    "filme", "fluxo", "folha", "fonte", "forte", "frase", "fruta", "gasto", "gesto", 
    "golpe", "grade", "grave", "grupo", "guia", "honra", "horta", "idoso", "jogar"]
    erradas = []
    palavra = random.choice(txt) #comando para escolher uma palavra da lista, primeiro
    #a biblioteca e o comando logo depois do ponto, com o nome da lista nos parênteses
    n_tentativa = 1 #começa na primeira tentativa
    acertou = False #começa false, e assim que ficar true, o programa para
    
    while (n_tentativa<=6 and acertou == False):
        tentativa = input(f"\nTentativa {n_tentativa}/6 | Escreva sua tentativa: ")
        for i in range(5):
            if(len(tentativa)<5 or len(tentativa)>5): #verifica se a palavra tem 5 letras, se não, ele não aceita a tentativa
                n_tentativa-=1
                print("Escreva uma palavra com 5 letras")
                break #breka o for e volta pro while sem completar a 5 letras
            elif(tentativa == palavra):
                print(f"{tentativa[i]}🟩")
                acertou = True #o true encerra o programa, já que o while só funciona se o acertou for false
            elif(tentativa[i] == palavra[i]):
                print(f"{tentativa[i]}🟩")
            elif(tentativa[i] in palavra): #usamos o comando in para verificar se algo está na variável
                print(f"{tentativa[i]}🟨")
            elif(tentativa[i] not in palavra): #ativa caso a letra na posição i não esteja
                print(f"{tentativa[i]}🟥")
            time.sleep(0.35)
        if(acertou==True):
            break
        if(len(tentativa)<5 or len(tentativa)>5) == False: #se a palavra não tiver menos que 5 e mais que 5, ele executa
            time.sleep(0.3)
            print("\n-----Tabela de letras que não estão-----")
        for i in range(5):
            if(len(tentativa)<5 or len(tentativa)>5): #verifica se a palavra tem 5 letras, se não, ele não adiciona na lista
                break
            elif(tentativa[i] not in palavra): #FAZER LISTA PARA AS LETRAS Q NAO ESTAO APARECEREM A CADA TENTATIVA E CONTINUAREM
                erradas.append(tentativa[i])
        if(len(tentativa)<5 or len(tentativa)>5)==False:
            print(erradas)
            print("----------------------------------------\n")
        n_tentativa+=1
        if(n_tentativa>6):
            time.sleep(0.5)
            print("\n---------------------------------")
            print("|----------VOCÊ PERDEU!---------|")
            print(f"|-----A palavra era: {palavra} -----|")
            print("---------------------------------\n")
    if(acertou == True):
        time.sleep(0.5)
        print("\n---------------------------------")
        print("|----------VOCÊ VENCEU!---------|")
        print("---------------------------------")

termo()
avaliar = False
avaliacao = input("Avalie o jogo de 1 a 5: ")
avaliacao = int(avaliacao)

while (avaliar == False):
    if (avaliacao >= 3):
        print("Obrigado por atribuir a nota ‪‪❤︎‬")
        avaliar = True
    elif (avaliacao < 3):
        print("Vai se fuder 𐐘💥╾╤デ╦︻ඞා")
        avaliar = True
    elif (avaliacao > 5):
        print("Obrigado por atribuir uma nota mais alta do que o permitido <3")
        avaliar = True
    else:
        print("Por favor escreva um número")
denovo = True
novamente = input("Deseja jogar novamente? ")
while (denovo == True):
    if(novamente == "sim" or novamente == "s" or novamente == "si" or novamente == "Sim" or novamente == "S"):
        termo()
    elif(novamente == "nao" or novamente == "não" or novamente == "no" or novamente == "n" or novamente == "NAO" or 
     novamente == "Não" or novamente == "Nao" or novamente == "NÃO" or novamente == "n"):
        print("Obrigado por jogar!")
        denovo = False
        break

    


"""
Cenas do jogo "A Caverna de Júlia".

Cada função representa uma cena. As verificações de ordem dos lugares
ficam logo antes da cena da vila.
"""

from dados import espacos, interior, estado
from funcoes import (
    separador, titulo, narrar, fala, pensamento, escolher, mostrar_inventario
)
from mapa import desenhar_mapa


# ABERTURA
def cena_abertura():
    titulo("A Caverna de Júlia")
    narrar(espacos["começo_vila"]["descricao"])
    mostrar_inventario()


# VERIFICAÇÕES DE ORDEM DOS LUGARES
# Pensamento mostrado quando falta cumprir cada requisito (chave = flag do estado).
_MENSAGENS_FALTA = {
    "visitou_padre":   "Antes de me embrenhar por aí, sinto que devia passar na Igreja primeiro...",
    "visitou_crianca": "Algo me diz para dar uma volta no Parque antes de seguir...",
    "visitou_casa":    "Não consigo seguir sem antes ver a Casa de Júlia primeiro...",
    "visitou_fazenda": "Eu sinto que tenho que ir para a Fazenda primeiro.",
}


def lugar_faltando(destino):
    """
    Verifica se o jogador pode ir até `destino`, com base nas `saidas`
    da vila no JSON: cada saída lista as flags de estado exigidas, na
    ordem em que devem ser cobradas.

    Retorna o pensamento do primeiro requisito ainda não cumprido,
    ou None se o acesso está liberado.
    """
    for flag in espacos["começo_vila"]["saidas"][destino]:
        if not estado[flag]:
            return _MENSAGENS_FALTA[flag]
    return None


# A VILA
def cena_vila():
    while True:
        opcoes = []
        for chave, dados in espacos["começo_vila"]["opcoes"].items():
            opcoes.append(dados["lugar"])

        # Mapa visual da vila (lugares e posições vêm do JSON)
        desenhar_mapa("começo_vila")
        idx = escolher(opcoes)
        destino = opcoes[idx]

        # Lugares livres — a ordem entre eles não importa
        if destino == "Igreja":
            cena_igreja()
        elif destino == "Parque":
            cena_parque()
        elif destino == "Casa de Júlia":
            cena_casa_julia()

        # Fazenda = PENÚLTIMO lugar (só após Igreja, Parque e Casa de Júlia)
        elif destino == "Fazenda":
            falta = lugar_faltando(destino)
            if falta:
                pensamento(falta)
            else:
                cena_fazenda()

        # Caverna = ÚLTIMO lugar (só após tudo, incluindo a Fazenda)
        elif destino == "Caverna":
            falta = lugar_faltando(destino)
            if falta:
                pensamento(falta)
            else:
                break


# IGREJA
def cena_igreja():
    titulo("Igreja")
    narrar(interior["Igreja"]["descricao"])

    fala("Padre",
         "Ah, olá meu jovem, você é novo por aqui, não é? Bem-vindo à vila. Eu sou o padre daqui.")
    fala("Você", "Olá, padre. O que é esse lugar?")
    fala("Padre",
         "É uma vila pequena e pacata, mas é nossa casa. Vivemos aqui há gerações, mas ultimamente tem sido difícil...")
    fala("Padre",
         "A Júlia, uma mulher que morava aqui, está sofrendo muito e está desaparecida. Ninguém a vê há dias.\n"
         "Ela era uma pessoa boa, mas depois de um incidente na caverna, as pessoas começaram a\n"
         "olhar torto para ela. Ela se isolou cada vez mais, e agora ninguém sabe onde ela está.")
    fala("Você", "O que aconteceu na caverna?")         
    fala("Padre",
         "Ela perdeu o marido, que era um minerador que sumiu \n"
         "depois de encontrar ouro na caverna. E pior: seu filho foi procurá-lo\n"
         "e também nunca voltou. Ninguém a viu recentemente. Estou preocupado com ela.")
    fala("Padre",
         "Por favor, se você encontrar com ela, ajude-a. Ela não tem mais ninguém, infelizmente.")

    estado["visitou_padre"] = True
    input("\n[Pressione Enter para sair da Igreja]")


# PARQUE
def cena_parque():
    desenhar_mapa("mapa2_parque", "PARQUE")
    narrar(interior["Parque"]["descricao"])

    idx = escolher(["Falar com a criança", "Ir embora"])
    if idx == 0:
        fala("Criança",
             "Sabe que tem ouro naquela caverna? Meu avô disse...\n"
             "Mas tem algo muito sombrio lá dentro. Algo que não é humano.\n"
             "Alguma coisa que ninguém descobriu ate hoje.")
        fala("Criança",
             "Os adultos não deixam a gente ir lá. Mas se você for...\n"
             "tome cuidado com o que você acha que viu. Nem tudo é o que parece.")
    estado["visitou_crianca"] = True
    input("\n[Pressione Enter para sair do Parque]")


# CASA DE JÚLIA
def cena_casa_julia():
    titulo("Casa de Júlia")
    narrar(interior["Casa de Júlia"]["descricao"])
    narrar(
        "A carta diz:\n"
        "Se alguém encontrar isto... não me procure. Prefiro ir na procura deles,\n"
        "do que continuar aqui, sozinha, humilhada por algo que nunca pedi e nunca.\n"
        "desejei a ninguém."
    )
    estado["visitou_casa"] = True
    input("\n[Pressione Enter para sair da Casa]")


# FAZENDA
def cena_fazenda():
    titulo("Fazenda")
    narrar(interior["Fazenda"]["descricao"])
    estado["visitou_fazenda"] = True
    input("\n[Pressione Enter para sair da Fazenda]")


# CAMINHO ATÉ A CAVERNA
def cena_caminho_caverna():
    titulo("Caminho para a Caverna")
    narrar(
        "Dois lenhadores aparecem quando você se aproxima da caverna.\n"
        "Eles parecem nervosos."
    )
    fala("Lenhador 1",
         "Você vai entrar aí? Nós também... mas isso é perigoso.\n"
         "Já perdemos gente nessa caverna. Fique com isso para te ajudar lá.")
    narrar("Ele te entrega uma 🔦 lanterna.")
    estado["itens"].append("lanterna")

    fala("Lenhador 1",
         "Eu fico aqui fora de guarda. Meu parceiro vai na frente e logo\n"
         "em seguida você entra.")

    narrar("Já na entrada da caverna, o segundo lenhador aparece das sombras.")
    fala("Lenhador 2",
         "Vai precisar disso lá dentro.")
    narrar("Ele coloca uma 🔪 faca em suas mãos e segue caminho com você.")
    estado["itens"].append("faca")

    mostrar_inventario()
    input("\n[Pressione Enter para entrar na Caverna]")


# DENTRO DA CAVERNA: FAZENDEIRO
def cena_fazendeiro():
    desenhar_mapa("mapa3_caverna_entrada", "CAVERNA — ENTRADA")
    narrar(espacos["mapa3_caverna_entrada"]["descricao"])
    fala("Fazendeiro", "Fique longe! Vocês não sabem o que está acontecendo aqui...")

    narrar("Vocês suspeitam dele. Você pode fazer uma pergunta.")
    perguntas = [
        "Por que há sangue em você?",
        "O que você estava fazendo aqui dentro?",
        "Você fez algo com Júlia?"
    ]
    respostas = [
        "Eu... Eu... Eu me machuquei numa rocha tentando sair, só queiria sair logo.",
        "Vim procurar minério como sempre faço. Mas ouvi algo e entrei em desespero!!!",
        "Júlia?! Quem é essa? Nem a conheço direito! Só quero ir embora, com licença, por favor!"
    ]

    idx = escolher(perguntas, prompt="Sua pergunta: ")
    estado["pergunta_feita"] = perguntas[idx]

    fala("Fazendeiro", respostas[idx])
    narrar("O fazendeiro vai embora apressado. Você fica com dúvidas e preocupado, mas continua.")
    input("\n[Pressione Enter para avançar na caverna]")


# DENTRO DA CAVERNA: JÚLIA
def cena_julia():
    desenhar_mapa("mapa5_caverna_interior", "CAVERNA — INTERIOR")
    narrar(espacos["mapa5_caverna_interior"]["descricao"])
    fala("Júlia",
         "Eu... eu vim até aqui para ficar perto deles.\n"
         "Meu marido, meu filho... ambos desapareceram aqui dentro.\n"
         "A vila me odiou por um ouro que nunca tive. Estou cansada de tudo isso.")

    narrar("Você percebe a gravidade da situação. O que você faz?")
    idx = escolher([
        "Ajudá-la a sair da caverna",
        "Recuar com medo e sair correndo"
    ])

    if idx == 0:
        fala("Você", "Vamos sair daqui. Eu te ajudo.")
        narrar(
            "Júlia hesita, mas aceita sua mão.\n"
            "Vocês caminham juntos em direção à saída da caverna."
        )
        estado["fim"] = "ajudar"
    else:
        fala("Você", "Eu... eu não sei o que fazer! Sinto muito.")
        narrar(
            "Você foge da caverna, perturbado.\n"
            "Júlia fica para trás, sozinha no escuro."
        )
        estado["fim"] = "sair"

    input("\n[Pressione Enter para continuar]")


# SAÍDA DA CAVERNA: ACUSAÇÃO (próprio argumento contra você)
def cena_acusacao():
    titulo("Caverna — Saída")
    narrar(
        "Quando você se aproxima da saída da caverna,\n"
        "uma pessoa qualquer aparece bloqueando o caminho.\n"
        "Ele olha para você e em seguida para a faca."
    )
    fala("Novo Fazendeiro",
         "Para aí! Você tem uma faca. Está coberto de sangue.\n"
         "O que você estava fazendo lá dentro?\n"
         "Um fazendeiro acabou de contar sobre você e manter distância,\n"
         "porque você é perigoso e está envolvido com o caso da Júlia.")

    narrar("Ele aponta para você e te acusa, igual você acusou o fazendeiro.")
    separador()
    print(f'  "{estado["pergunta_feita"]}"')
    separador()

    narrar("Você pode responder o que quiser. Digite sua resposta:")
    resposta = input("Sua resposta: ")

    fala("Novo Fazendeiro",
         f"{resposta} — Isso é exatamente o que o fazendeiro diria. Vou chamar os outros agora mesmo"
    )

    narrar(
        "Ele escolhe exatamente a mesma opção que você escolheu\n"
        "para acusar o primeiro fazendeiro. Sem provas. Sem ouvir.\n"
        "Apenas suspeitando."
    )
    input("\n[Pressione Enter para ver o final]")


# FINAIS
def cena_final():
    titulo("Final")

    if estado["fim"] == "ajudar":
        narrar(
            "Você conseguiu sair com Júlia. Ela está viva.\n"
            "A vila a olha com surpresa — ninguém esperava que ela voltasse.\n\n"
            "A acusação do fazendeiro e de você se dissolve quando Júlia conta o que aconteceu.\n"
            "Mas a desconfiança da vila ainda paira no ar.\n\n"
            "Você percebe: o verdadeiro monstro da caverna nunca foi sobrenatural.\n"
            "Foi o julgamento. A desconfiança. A falta de compaixão."
        )
    else:
        narrar(
            "Você está na praça da vila, sendo apontado pelos moradores.\n"
            "Júlia ficou lá dentro. Ninguém sabe o que aconteceu com ela.\n\n"
            "E agora você entende o que o fazendeiro sentiu quando você o acusou:\n"
            "inocente, mas incapaz de provar."
        )

    separador("═")
    print()
    print("  O verdadeiro monstro sempre foi a desconfiança humana.")
    print("  O julgamento sem provas. As escolhas morais que fazemos")
    print("  sem parar para ouvir o outro lado.")
    print()
    separador("═")
    print()
    print("               FIM DE JOGO ")
    print()
    separador("═")

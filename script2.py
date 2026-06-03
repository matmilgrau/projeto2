import json

espacos = {"estrada" : {
              "1" : {"lugar" : "casa", "pos" : [34,10]},
              "2" : {"lugar" : "igreja", "pos" : [5,10]},
              "3" : {"lugar" : "campos", "pos" : [20,18]}
          },
          "campos" : {
              "1" : {"conversar" : "criança", "pos" : [5,10]},
              "2" : {"lugar" : "caverna", "pos" : [20,18]}
          },
          "caverna" : {
              "1" : {"conversar" : "fazendeiro", "pos" : [5,10]},
              "2" : {"lugar" : "avançar", "pos" : [20,18]},
          },
          "caverna2" : {
              "1" : {"lugar" : "esquerda", "pos" : [5,10]},
              "2" : {"lugar" : "direito", "pos" : [34,10]},
              "3" : {"lugar" : "reto", "pos" : [20,18]}
          },
          "reto1" : {
              "1" : {"conversar" : "fazendeiro2", "pos" : [20,18]}
          },
          "fazendeiro" : {
              "1" : {"ação" : "matar"},
              "2" : {"ação" : "perdoar"}
          },
          "reto2" : {
              "1" : {"lugar" : "avançar"}
          },
          "J" : {
              "1" : {"conversar" : "j"}
          }}

interior = {"interior" :
                { "1" : {"casa" : "carta escrita a mão", "pos" : [20,18]},
                  "2" : {"casa" : "faca", "pos" : [34,10]},
                  "3" : {"igreja" : "padre", "pos" : [20,18]}}}
objetos = {"objeto" :
               { "1" : {"carta" : "Meu nome é -----. Meu marido nos --------- e meu ----- foi atrás procurar ele."
                                  "Não ------- mais ----- nessa vida de desgraças, por ----, vou acabar com minha"
                                  "----, custe o que custar. Ass: J---- "},
                 "2" : {"faca" : "você obteve uma faca"}}}
saidas = {"saida" :
              { "1" : {"igreja" : "saida", "pos" : [20,5]},
                "2" : {"casa" : "saida", "pos" : [20,5]},
                "3" : {"campo" : "estrada", "pos" : [20,5]},
                "4" : {"caverna1" : "campo", "pos" : [20,5]},
                "5" : {"esquerda" : "caverna2", "pos" : [34,10]},
                "6" : {"direita" : "caverna2", "pos" : [5,10]},
                "7" : {"caverna2" : "caverna1", "pos" : [20,5]},
                "8" : {"reto1" : "caverna2", "pos" : [20,5]},
                "9" : {"reto2" : "reto1", "pos" : [20,5]}}}
pessoas = {"pessoa":
               {"1" : {"padre" : "Algumas pessoas dessa vila se corromperam, umas por ganância, outras por obssessões..." , "pos" : [5,10]},
                "2" : {"criança" : "Não sei se você sabe, mas há rumores de que aquela caverna é assombrada. Apenas ouse ir lá se tiver muita coragem.", "pos" : [5,10]},
                "3" : {"fazendeiro1" : "Estou nessa caverna pois ouvi alguns gritos daqui de fora. Receio que seja da Júlia, uma das nossas moradoras que esteve envolvida em problemas recentemente", "pos" : [5,10]}}}

falas = {"fala":
             {"1" : {"fazendeiro2" : "Olá..."}, #após o olá, o player ter uma opção na tela para escolher a fala, que diz "por que você está segurando uma faca com sangue?"
              "2" : {"fazendeiro2" : "Eu sei que isso pode parecer estranho, mas você precisa confiar em mim!"}, #o player terá 3 opções de escolher uma pergunta na tela, e a pergunta que ele escolher, vai se repetir no final do jogo
              "3.1" : {"fazendeiro2" : "Eu estava apenas tentando ajudar ela."}, #a 1° pergunta vai ser: o que você estava fazendo lá dentro?
              "3.2" : {"fazendeiro2" : "Da Júlia, mas eu posso explicar!"}, #a 2° pergunta vai ser: de quem são esses gritos no fundo da caverna?
              "3.3" : {"fazendeiro2" : "Sou Carlos, um fazendeiro que só queria ajudá-la."},#a 3° pergunta vai ser: quem é você?
               #depois da resposta de uma das perguntas, o player vai falar que não acredita na resposta do fazendeiro
              "4" : {"fazendeiro2" : "Por favor acredite!"}, #após essa fala, aparecerão duas opções na tela: matar ou perdoar. você pode matar o fazendeiro ou matá-lo
              "5.1" : {"fazendeiro2" : "Eu só queria ajudar..."}, #fala do fazendeiro se você matar ele
              "5.2" : {"fazendeiro2" : "Obrigado por acreditar em mim!"}}} #fala do fazendeiro se você perdoar ele

falas2 = {"fala":
              {"1" : {"julia" : "Quem é você? Porque vocês insistem em vir até aqui?!"}, #nesse momento, o player não vai dizer nada, apenas ouvir o que ela tem a dizer
               "2" : {"julia" : "Já não bastava eu ter perdido meu filho e meu marido, agora vocês querem se perder também?"},
               "3" : {"julia" : "Essa vila é um completo inferno. Todas as pessoas pecam e mentem entre si, todas gananciosas e nojentas."},
               "4" : {"julia" : "E por que você está parado ai? eu quero que você vá embora, eu não quero que você me ajude!"}, #nesse momento, júlia vai começar a jogar sangue no player, deixando ele manchado
               "5" : {"julia" : "*Júlia arremessa sangue em você, te deixando manchado*"},
               "6" : {"julia" : "Apenas vá embora, meu filho morreu nessa mina procurando seu próprio pai que nos abandonou. Eu só quero acabar com esse sofrimento"}}} #aqui, aparecerá apenas a opção do player ir embora

falas3 = {"fala":
              {"1" : {"fazendeiro3" : "Por que você está segurando uma faca com sangue?"}, #o player vai ter uma opção na tela pra dizer "Eu sei que isso pode parecer estranho, mas você precisa confiar em mim!"
               "2" : {"fazendeiro3" : ""}, #nessa caixa de pergunta, o fazendeiro3 vai fazer a mesma pergunta que o player escolheu, por isso, é preciso criar uma variável para armazenar a pergunta
               "3" : {"fazendeiro3" : "Eu não acredito na sua resposta..."},
               #a escolha 4.1 e 4.2 vão ser escolhidas baseado no que o player escolheu com o 2° fazendeiro
               "4.1" : {"fazendeiro3" : "então, você não me deixa outra escolha a não ser te matar"},
               "4.2" : {"fazendeiro3" : "mas eu vou te perdoar."}}}


#usar a chave para gerar o valor. depois, vou corrigir a lógica para que, quando uma chave for ativada, seu valor apareça na tela. para não esquecer, chave : valor

jogo = True
while(jogo == True):

    x = input("Escolha a opção para interagir entre casa, igreja ou parar ")
    x = str(x)
    if (x=="casa"):
        print(espacos["estrada"]["1"]["lugar"])
    elif (x=="igreja"):
        print(saidas["saida"]["1"]["igreja"])
        print(interior["interior"]["2"]["igreja"])
    elif(x=="parar"):
        jogo = False


LARGURA = 40
ALTURA = 20
#espaços vai chamar o dicionario, ai depois voce vai selecionar a chave entre o começo, mapa2, etc., depois, voce escolhe a chave entre os numeros e pois qual chave chamar
#fazer mais um subdicionario para os espaços internos dos lugares, como casa, igreja, etc.
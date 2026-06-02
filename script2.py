import json

espacos = {"começo" : {
              "1" : {"lugar" : "casa", "pos" : [34,10]},
              "2" : {"lugar" : "igreja", "pos" : [5,10]},
              "3" : {"lugar" : "campos", "pos" : [20,18]}
          },
          "mapa2" : {
              "1" : {"lugar" : "criança", "pos" : [5,10]},
              "2" : {"lugar" : "caverna", "pos" : [20,18]}
          },
          "mapa3" : {
              "1" : {"lugar" : "fazendeiro", "pos" : [5,10]},
              "2" : {"lugar" : "avançar", "pos" : [20,18]},
          },
          "mapa4" : {
              "1" : {"lugar" : "esquerda", "pos" : [5,10]},
              "2" : {"lugar" : "direito", "pos" : [34,10]},
              "3" : {"lugar" : "reto", "pos" : [20,18]}
          },
          "mapa5" : {
              "1" : {"lugar" : "julia", "pos" : [20,18]}}}

interior = {"interior" :
                { "1" : {"casa" : "carta escrita a mão", "pos" : [20,18]},
                  "2" : {"igreja" : "padre", "pos" : [20,18]},
                  }}

x = input("Escolha a opção para interagir ")
if (x=="casa"):
    print(espacos["comeco"]["1"]["lugar"])


LARGURA = 40
ALTURA = 20

print(espacos["mapa2"]["1"]["lugar"])
#espaços vai chamar o dicionario, ai depois voce vai selecionar a chave entre o começo, mapa2, etc., depois, voce escolhe a chave entre os numeros e pois qual chave chamar
#fazer mais um subdicionario para os espaços internos dos lugares, como casa, igreja, etc.
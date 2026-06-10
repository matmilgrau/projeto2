"""
Ponto de entrada do jogo "A Caverna de Júlia".

Execute com:  python3 main.py
"""

from dados import reset_estado
from cenas import (
    cena_abertura,
    cena_vila,
    cena_caminho_caverna,
    cena_fazendeiro,
    cena_julia,
    cena_acusacao,
    cena_final,
)


def main():
    # Resetar estado (útil para jogar de novo)
    reset_estado()

    # Sequência principal
    cena_abertura()
    cena_vila()
    cena_caminho_caverna()
    cena_fazendeiro()
    cena_julia()
    cena_acusacao()
    cena_final()


if __name__ == "__main__":
    main()

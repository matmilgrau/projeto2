"""
Mapa visual dos lugares.

Lê as coordenadas `pos` de cada lugar em `espacos[<nome>]` (no espaço
LARGURA x ALTURA definido no JSON) e desenha uma moldura em arte ASCII,
no estilo da tela "A VILA — para onde ir?".
"""

from dados import espacos, LARGURA, ALTURA

INNER = 64          # largura interna útil (colunas de conteúdo)
LINHAS = 9          # altura interna (linhas de conteúdo)


def _escala_x(x):
    """Converte a coordenada x do JSON para a coluna na tela."""
    return round(x / LARGURA * (INNER - 1))


def _escala_y(y):
    """Converte a coordenada y do JSON para a linha na tela."""
    return round(y / ALTURA * (LINHAS - 1))


def _imprimir_moldura(titulo_texto, linhas):
    """Envolve as linhas de conteúdo numa moldura dupla com título."""
    larg = INNER
    print("╔" + "═" * (larg + 4) + "╗")          # borda externa
    print("║ ╔" + "═" * larg + "╗ ║")             # borda interna
    print("║ ║" + titulo_texto.center(larg) + "║ ║")
    print("║ ╠" + "═" * larg + "╣ ║")
    for linha in linhas:
        print("║ ║" + linha + "║ ║")
    print("║ ╚" + "═" * larg + "╝ ║")
    print("╚" + "═" * (larg + 4) + "╝")


def desenhar_mapa(nome_espaco="começo_vila", titulo_texto="A VILA — para onde ir?"):
    """
    Desenha o mapa de um espaço usando as posições do JSON.

    nome_espaco: chave dentro de `espacos` (ex.: "começo_vila", "mapa4_caverna_caminho"...).
    """
    lugares = espacos[nome_espaco]["opcoes"]

    # tela em branco
    tela = [[" "] * INNER for _ in range(LINHAS)]

    for chave, dados in lugares.items():
        x, y = dados["pos"]
        rotulo = f"[{chave}] {dados['lugar']}"

        col = _escala_x(x)
        lin = _escala_y(y)

        # mantém o rótulo inteiro dentro da área visível
        col = max(0, min(col, INNER - len(rotulo)))
        lin = max(0, min(lin, LINHAS - 1))

        for i, ch in enumerate(rotulo):
            tela[lin][col + i] = ch

    _imprimir_moldura(titulo_texto, ["".join(linha) for linha in tela])


if __name__ == "__main__":
    # Demonstração: desenha cada espaço definido no JSON
    titulos = {
        "começo_vila":            "A VILA — para onde ir?",
        "mapa2_parque":           "PARQUE",
        "mapa3_caverna_entrada":  "CAVERNA — ENTRADA",
        "mapa4_caverna_caminho":  "CAVERNA — QUAL CAMINHO?",
        "mapa5_caverna_interior": "CAVERNA — INTERIOR",
    }
    for nome in espacos:
        desenhar_mapa(nome, titulos.get(nome, nome.upper()))
        print()

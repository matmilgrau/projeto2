"""
Funções auxiliares de exibição e interação com o jogador.
"""

from dados import estado


def separador(char="─", n=50):
    print(char * n)


def titulo(texto):
    separador("═")
    print(f"  {texto.upper()}")
    separador("═")


def narrar(texto):
    """Imprime texto narrativo com destaque."""
    print(f"\n{texto}\n")


def fala(personagem, texto):
    """Imprime fala de um personagem."""
    print(f'\n[{personagem.upper()}] "{texto}"')


def pensamento(texto):
    """Imprime um pensamento interno do personagem principal."""
    print(f"\n  💭 (você pensa) {texto}\n")


def escolher(opcoes, prompt="Sua escolha: "):
    """
    Exibe opções numeradas e retorna o índice escolhido.
    opcoes: lista de strings
    """
    while True:
        print()
        for i, op in enumerate(opcoes, 1):
            print(f"  [{i}] {op}")
        print()
        try:
            resp = int(input(prompt))
            if 1 <= resp <= len(opcoes):
                return resp - 1          # índice 0-based
            print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Digite um número.")


def mostrar_inventario():
    if estado["itens"]:
        print(f"  🎒 Inventário: {', '.join(estado['itens'])}")
    else:
        print("  🎒 Inventário: vazio")

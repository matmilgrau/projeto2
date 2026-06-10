"""
Estrutura de dados do jogo.

Carrega tudo do arquivo `dados_jogo.json` e expõe as variáveis
compartilhadas por todos os módulos do jogo.
"""

import json
from pathlib import Path

# Caminho do JSON relativo a este arquivo (funciona de qualquer pasta)
_CAMINHO_JSON = Path(__file__).with_name("dados_jogo.json")

with open(_CAMINHO_JSON, encoding="utf-8") as f:
    _dados = json.load(f)

espacos  = _dados["espacos"]
interior = _dados["interior"]
estado   = _dados["estado"]      # inventário e progresso do jogador
LARGURA  = _dados["LARGURA"]
ALTURA   = _dados["ALTURA"]


def reset_estado():
    """
    Recarrega o estado inicial a partir do JSON.

    Importante: limpa e atualiza o MESMO objeto `estado`, em vez de criar
    um novo. Assim os outros módulos que fizeram `from dados import estado`
    continuam enxergando as alterações.
    """
    with open(_CAMINHO_JSON, encoding="utf-8") as f:
        estado.clear()
        estado.update(json.load(f)["estado"])

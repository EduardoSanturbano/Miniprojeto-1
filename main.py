"""Modo batch: lê consultas.json, responde em ordem, grava respostas.json.

Uso: python main.py consultas.json respostas.json
"""
from catalogo import Catalogo
import json
import sys
from pathlib import Path

def main():
    caminho_consultas = sys.argv[1]
    caminho_respostas = sys.argv[2]

    pasta_do_projeto = Path(__file__).parent
    caminho_catalogo = pasta_do_projeto / "catalogo_final.json"
    catalogo = Catalogo(str(caminho_catalogo))

    with open(caminho_consultas, "r", encoding="utf-8") as arquivo:
        dados_consultas = json.load(arquivo)

    respostas = {}

    for consulta in dados_consultas["consultas"]:
        tipo = consulta["tipo"]
        parametros = consulta["parametros"]
        metodo = getattr(catalogo, tipo)
        resposta = metodo(**parametros)
        respostas[str(consulta["id"])] = resposta

    with open(caminho_respostas, "w", encoding="utf-8") as arquivo:
        json.dump(respostas, arquivo, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
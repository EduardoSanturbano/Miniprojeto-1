"""A classe Catalogo. Leia o README.md antes de começar.

Esta é a peça central do projeto: carrega o JSON uma vez, constrói os
índices no __init__ e expõe os 16 métodos que o main.py e o cli.py usam.
"""
import json
from collections import deque

class Catalogo:
    def __init__(self, caminho_json: str): 
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        self.conteudos = dados["conteudos"]
        self.usuarios = dados["usuarios"]
    
        self.fila = deque()
        self.conteudos_por_id = {}
        for conteudo in self.conteudos:
            self.conteudos_por_id[conteudo["id"]] = conteudo

    # --- usuários e playlists ---
    def listar_usuarios(self) -> list[str]:
        nome = []
        for user in self.usuarios:
            nome.append(user["nome"])
        return sorted(nome)

    def buscar_usuario_por_nome(self, nome: str) -> str | None:
        self.nome = nome
        nome_alvo = nome.lower()
        for i in self.usuarios:
            nome_dicionario = i["nome"].lower()
            if nome_dicionario == nome_alvo:
                return i["id"]
        return None

    def playlist_de(self, usuario_id: str) -> list[str] | None:
        for i in self.usuarios:
            if i["id"] == usuario_id:
                return i["playlist"]
        return None

    def conteudo_na_posicao(self, usuario_id: str, posicao: int) -> str | None:
        playlist = self.playlist_de(usuario_id)
        if playlist is None:
            return None
        elif posicao < 0 or posicao >= len(playlist):
            return None
        else:
            return playlist[posicao]

    def intersecao_playlists(self, usuario_ids: list[str]) -> list[str]:
        if len(usuario_ids) == 0:
            return []
        conteudos_em_comum = None
        for usuario_id in usuario_ids:
            playlist = self.playlist_de(usuario_id)
            if playlist is None:
                return []
            if conteudos_em_comum is None:
                conteudos_em_comum = set(playlist)
            else:
                conteudos_em_comum = conteudos_em_comum.intersection(playlist)
        return sorted(conteudos_em_comum)
                        
    # --- dados de um conteúdo ---
    def rating_de(self, conteudo_id: str) -> float | None:
        conteudo = self._conteudo_por_id(conteudo_id)
        if conteudo is None:
            return None
        rating = conteudo.get("rating")
        if rating is None:
            return None
        return float(rating)

    def duracao_total_de(self, conteudo_id: str) -> int | None:
        conteudo = self._conteudo_por_id(conteudo_id)
        if conteudo is None:
            return None
        if conteudo["tipo"] == "musica":
            return conteudo["duracao_seg"]
        total_segundos = 0
        for faixa in conteudo["faixas"]:
            duracao = faixa["duracao_seg"]
            if duracao is not None:
                total_segundos += duracao
        return total_segundos


    def generos_de(self, conteudo_id: str) -> list[str] | None:
        conteudo = self._conteudo_por_id(conteudo_id)
        if conteudo is None:
            return None
        generos_achatados = self._achatar_generos(conteudo["generos"])
        return sorted(generos_achatados)

    def plataformas_de(self, conteudo_id: str) -> list[str] | None:
        conteudo = self._conteudo_por_id(conteudo_id)
        if conteudo is None:
            return None
        plataformas = conteudo.get("plataformas", [])
        return sorted(plataformas)

    def data_adicionado_de(self, conteudo_id: str) -> str | None:
        conteudo = self._conteudo_por_id(conteudo_id)
        if conteudo is None:
            return None
        data = conteudo["data_adicionado"]
        if "/" in data:
            dia, mes, ano = data.split("/")
            return f"{ano}-{mes}-{dia}"
        return data


    def execucoes_de(self, conteudo_id: str) -> int | None:
        conteudo = self._conteudo_por_id(conteudo_id)
        if conteudo is None:
            return None
        engajamento = conteudo.get("engajamento")
        if engajamento is None:
            return None
        execucoes = engajamento["execucoes"]
        if isinstance(execucoes, str):
            execucoes = execucoes.replace(",", "")
        return int(execucoes)


    def conteudos_do_genero(self, genero: str) -> list[str]:
        ids_encontrados = []
        for conteudo in self.conteudos:
            generos_do_conteudo = self._achatar_generos(conteudo["generos"])
            if genero in generos_do_conteudo:
                ids_encontrados.append(conteudo["id"])
        return sorted(ids_encontrados)


    # --- fila de reprodução ---
    def enfileirar(self, conteudo_id: str) -> bool:
        if conteudo_id not in self.conteudos_por_id:
            return False
        self.fila.append(conteudo_id)
        return True
    def proximo(self) -> str | None: 
        if not self.fila:
            return None
        return self.fila.popleft()
    def fila_atual(self) -> list[str]:
        return list(self.fila)

    # métodos auxíliares:
    def descricao_conteudo(self, conteudo_id: str) -> str | None:
        for conteudo in self.conteudos:
            if conteudo["id"] == conteudo_id:
                titulo = conteudo["titulo"]
                artista = conteudo["artista"]
                tipo = conteudo["tipo"]
                return f"{titulo}, de {artista} ({tipo})"
        return None
    
    def _conteudo_por_id(self, conteudo_id: str) -> dict | None:
        return self.conteudos_por_id.get(conteudo_id)

    def _achatar_generos(self, generos) -> list[str]:
        resultado = []
        if isinstance(generos, str):
            return [generos]
        if isinstance(generos, list):
            for genero in generos:
                resultado.extend(self._achatar_generos(genero))
        return resultado

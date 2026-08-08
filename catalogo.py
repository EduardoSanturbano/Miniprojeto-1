"""A classe Catalogo. Leia o README.md antes de começar.

Esta é a peça central do projeto: carrega o JSON uma vez, constrói os
índices no __init__ e expõe os 16 métodos que o main.py e o cli.py usam.
"""
class Catalogo:
    def __init__(self, caminho_json: str): 
        self.caminho_json = caminho_json
        fila = []

    # --- usuários e playlists ---
    def listar_usuarios(self) -> list[str]:
        print()

    def buscar_usuario_por_nome(self, nome: str) -> str | None:
        

    def playlist_de(self, usuario_id: str) -> list[str] | None:

    def conteudo_na_posicao(self, usuario_id: str, posicao: int) -> str | None:

    def intersecao_playlists(self, usuario_ids: list[str]) -> list[str]:


    # --- dados de um conteúdo ---
    def rating_de(self, conteudo_id: str) -> float | None: ...
    def duracao_total_de(self, conteudo_id: str) -> int | None: ...
    def generos_de(self, conteudo_id: str) -> list[str] | None: ...
    def plataformas_de(self, conteudo_id: str) -> list[str] | None: ...
    def data_adicionado_de(self, conteudo_id: str) -> str | None: ...
    def execucoes_de(self, conteudo_id: str) -> int | None: ...
    def conteudos_do_genero(self, genero: str) -> list[str]: ...

    # --- fila de reprodução ---
    def enfileirar(self, conteudo_id: str) -> bool:
        if conteudo_id not in catalogo:
            return False
        fila.insert(conteudo_id)
        return True
    def proximo(self) -> str | None: 
        try:
            return lista.pop[0]
        except IndexError:
            return None
    def fila_atual(self) -> list[str]:
        return lista

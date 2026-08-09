"""Menu interativo no terminal.

Uso: python cli.py catalogo_final.json
"""
from catalogo import Catalogo
import sys
catalogo = Catalogo(sys.argv[1])

while True:
    print("""
        TrilhaSonora
        ============
        1. Listar todos os usuários
        2. Ver playlist completa de um usuário
        3. Conteúdo na posição N da playlist
        4. Interseção de playlists (N usuários)
        5. Dados de um conteúdo (rating, duração, gêneros, plataformas, data, execuções)
        6. Conteúdos de um gênero
        7. Enfileirar conteúdo na fila de reprodução
        8. Tocar próximo da fila
        9. Ver fila atual
        0. Sair
        >
    """)
    opcao = int(input())
    match opcao:
        case 1:
            catalogo.listar_usuarios()
        case 2:
            nome = input("Nome do usuário: ")
            catalogo.playlist_de(catalogo.buscar_usuario_por_nome(nome))
        case 3:
            nome = input("Nome do usuário: ")
            posicao = int(input("Posição: "))
            catalogo.conteudo_na_posicao(catalogo.buscar_usuario_por_nome(nome), posicao)
        case 4:
            nomes = list(map(str, input("Nomes dos usuários separados por vírgula (ex.: Nicholas, Uchoa): ").split(", ")))
            usuario_ids = list(map(buscar_usuario_por_nome, nome))
            ids_em_comum = catalogo.intersecao_playlists(usuarios_ids)
            if len(ids_em_comum) == 0:
                print("Não há conteúdos em comum.")
            else:
                print("Conteúdos em comum:")
                for conteudo_id in ids_em_comum:
                    descricao = catalogo.descricao_conteudo(conteudo_id)
                    print(descricao)
        case 5:
            conteudo_id = input("ID do conteúdo (ex.: t000000): ")
            catalogo.rating_de(conteudo_id)
            catalogo.duracao_total_de(conteudo_id)
            catalogo.generos_de(conteudo_id)
            catalogo.plataformas_de(conteudo_id)
            catalogo.data_adicionado_de(conteudo_id)
            catalogo.execucoes_de(conteudo_id)
        case 6:
            genero = input("Gênero (ex.: Pop): ")
            catalogo.conteudos_do_genero(genero)
        case 7:
            conteudo_id = input("ID do conteúdo pra enfileirar (ex.: t000000): ")
            catalogo.enfileirar(conteudo_id)
        case 8:
            catalogo.proximo()
        case 9:
            catalogo.fila_atual()
        case 0:
            break
        case _:
            print("Opção inválida")
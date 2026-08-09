"""Menu interativo no terminal.

Uso: python cli.py catalogo_final.json
"""
from catalogo import Catalogo
import sys
def main():
    if len(sys.argv) != 2:
        print("Uso: py cli.py catalogo_final.json")
        return
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
>""")
        opcao = int(input())
        match opcao:
            case 1:
                usuarios = catalogo.listar_usuarios()
                print("\nUsuários cadastrados:")
                for numero, nome in enumerate(usuarios, start=1):
                    print(f"{numero}. {nome}")
            case 2:
                nome = input("Nome do usuário: ").strip()
                usuario_id = catalogo.buscar_usuario_por_nome(nome)

                if usuario_id is None:
                    print("Usuário não encontrado.")
                else:
                    playlist = catalogo.playlist_de(usuario_id)

                    for conteudo_id in playlist:
                        print(catalogo.descricao_conteudo(conteudo_id))
            case 3:
                nome = input("Nome do usuário: ").strip()
                usuario_id = catalogo.buscar_usuario_por_nome(nome)
                if usuario_id is None:
                    print("Usuário não encontrado.")
                else:
                    try:
                        posicao = int(input("Posição: "))
                        conteudo_id = catalogo.conteudo_na_posicao(
                            usuario_id,
                            posicao - 1
                        )
                        if conteudo_id is None:
                            print("Posição inválida.")
                        else:
                            print(catalogo.descricao_conteudo(conteudo_id))
                    except ValueError:
                        print("Digite uma posição numérica.")
            case 4:
                texto_nomes = input("Nomes separados por vírgula: ")
                nomes = texto_nomes.split(",")
                usuario_ids = []
                for nome in nomes:
                    usuario_id = catalogo.buscar_usuario_por_nome(nome.strip())
                    if usuario_id is None:
                        print(f"Usuário não encontrado: {nome.strip()}")
                        break
                    usuario_ids.append(usuario_id)
                else:
                    ids_em_comum = catalogo.intersecao_playlists(usuario_ids)
                    if len(ids_em_comum) == 0:
                        print("Não há conteúdos em comum.")
                    else:
                        for conteudo_id in ids_em_comum:
                            print(catalogo.descricao_conteudo(conteudo_id))
            case 5:
                conteudo_id = input("ID do conteúdo (ex.: t000000): ").strip()
                descricao = catalogo.descricao_conteudo(conteudo_id)
                if descricao is None:
                    print("Conteúdo não encontrado.")
                else:
                    print(f"\n{descricao}")
                    print(f"Rating: {catalogo.rating_de(conteudo_id)}")
                    print(f"Duração total: {catalogo.duracao_total_de(conteudo_id)} segundos")
                    print(f"Gêneros: {', '.join(catalogo.generos_de(conteudo_id))}")
                    print(f"Plataformas: {', '.join(catalogo.plataformas_de(conteudo_id))}")
                    print(f"Data adicionado: {catalogo.data_adicionado_de(conteudo_id)}")
                    execucoes = catalogo.execucoes_de(conteudo_id)
                    if execucoes is not None:
                        print(f"Execuções: {execucoes}")
            case 6:
                genero = input("Gênero: (Ex.: Pop): ").strip()
                conteudos = catalogo.conteudos_do_genero(genero)
                if len(conteudos) == 0:
                    print("Nenhum conteúdo encontrado.")
                else:
                    for conteudo_id in conteudos:
                        print(catalogo.descricao_conteudo(conteudo_id))
            case 7:
                conteudo_id = input("ID do conteúdo pra enfileirar (ex.: t000000): ")
                catalogo.enfileirar(conteudo_id)
            case 8:
                conteudo_id = catalogo.proximo()
                if conteudo_id is None:
                    print("A fila está vazia.")
                else:
                    print(catalogo.descricao_conteudo(conteudo_id))
            case 9:
                fila = catalogo.fila_atual()
                if len(fila) == 0:
                    print("A fila está vazia.")
                else:
                    for conteudo_id in fila:
                        print(catalogo.descricao_conteudo(conteudo_id))
            case 0:
                break
            case _:
                print("Opção inválida")

if __name__ == "__main__":
    main()
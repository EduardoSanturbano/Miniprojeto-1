# Decisões de Modelagem

Criei a class Catalogo:
Modelei os métodos da fila de reprodução;
Desenvolvi o cli usando match case e as funções de cada caso;
Verifiquei os inputs durante o funcionamento do programa pra implementar no cli;
Modelei os outros métodos adaptando para tratar possíveis sujeiras;
Criei um método auxiliar: "descricao_conteudo" para transformar os ID's das músicas em nomes no cli;
Ajustei o cli pra tratar erros;
Criar a main foi difícil, mesmo já desenvolvendo a lógica no catálogo os comandos da main eram totalmente novos pra mim.
Criei um método auxiliar: "_conteudo_por_id" para transformar os ID's das músicas em nomes no cli;
Criei um método auxiliar: "_achatar_generos" para transformar os ID's das músicas em nomes no cli;
Corrigi erros de sintaxe.

# Conhecimentos consolidados

"def execucoes_de(self, conteudo_id: str) -> int | None: ..."
: str - recebe conteudo_id como string
-> int | None: - o método pode retorar inteiro ou none
... - é uma elipsis (nesse caso indica uma implementação omitida)

fila.insert(posição, objeto)

git status
git add .
git commit -m "bla bla bla"
git push origin main (main é o nome da branch)

match case:
    case 1:
        print("arroz")
    case _:
        print("default")

with open(caminho_json, "r", encoding="utf-8") as arquivo:
abrir o json recebido na hora da criação da classe no modo read e nomeado como um arquivo (facilita na hora de manipular)

dados = json.load(arquivo)
eu salvei os dados do arquivo na váriavel com o json.load

o JSON funciona como um dicionário com chaves
self.conteudos = dados["conteudos"]
self.usuaridos = dados["usuarios"]
conteudos e usuarios são as chaves principais

conjunto = set(lista) - cria uma cópia sem repetições de elementos
a.intersection(b) - retorna a interseção entra a e b

popleft() deleta o primeiro elemento

""" """ - aspas triplas para imprimir bloco

# Dificuldades encontradas

Primeiro eu fiquei sem entender o que escrever em cada arquivo (catalogo, cli e main), mas seguindo o README eu consegui construir parte por parte e entender suas respectivas funções.

Desenvolvendo a parte da fila de reprodução eu percebi que o código exemplo do site retorna strings junto com as request, fiquei sem saber exatamente em que parte colocar essas strings então coloquei nos inputs do cli.

Eu não tinha entendido o papel do JSON e o que vocês queriam quando pediam para "carregar" ele.

Fiquei confuso, pois não sabia como obter informações de arquivos para construir as funções do catálogo, mas foi ai que eu percebi pra que os JSON "catalogo" serviam.

Demorei pra entender que meus dados foram organizados em "conteúdos" e "usuários" dentro dos JSON, eu estava sem saber como modelar os métodos por causa disso. Depois que você desenvolve o init e a primeira função fica tudo mais tranquilo.

É mentira, implementar os outros métodos não foi nada tranquilo... e eu não sabia que precisava importar json e sys.

Muita coisa eu tava vendo pela primeira vez enquanto implementava o main, então eu fiquei com algumas dúvidas desenvolvendo a lógica.

Entender pra que esse "deque" servia não foi nada intuitivo, aplicar ele foi pior ainda.

Eu não estava entendendo a função do gabarito_publico.json e do consultas.json até chegar no main.






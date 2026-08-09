# Decisões de Modelagem

Criei a class Catalogo;
Modelei os métodos da fila de reprodução;
Desenvolvi o cli usando match case e as funções de cada caso;
Verifiquei os inputs durante o funcionamento do programa pra implementar no cli;

Modelei os outros métodos adaptando para tratar possíveis sujeiras;
Ajustei o cli pra tratar erros;
Criar a main foi fácil, uma vez que eu já desenvolvi a lógica no catálogo e só precisei repassar parâmetros.

# Diário

Querido diário, o fato da classe Catalogo ter o C maiusculo me incomoda. O fato de João ter adiado o prazo me conforta.
Querido diário, fiquei muito feliz quando vi que vocês deram a class Catalogo pronta... Eu estava desenvolvendo ela com base na lógica, mas isso vai me ajudar muito.
Querido diário, eu não li em canto algum que era proibido escrever um diário.

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

# Dificuldades encontradas

No começo eu não sabia nem quem eu era, mas as coisas foram dando certo.

Primeiro eu fiquei sem entender em qual dos arquivos (catalogo, cli e main) eu escrevia as classes do class Catalogo, mas interpretando com calma e sem medo de ter que programar vários arquivos eu percebi que é na propria catalogo.py.

Desenvolvendo a parte da fila de reprodução eu percebi que o código exemplo site retorna strings junto com as request, eu acho que isso é implementado no cli porque nem todos os metodos retornam strings.

Como assim a Catalogo "carrega o JSON" e "constroi os índices no init"? Acredito que vou descobrir + pra frente.

Fiquei confuso, pois não sabia como obter informações de arquivos para construir as funções do catálogo além das funções da fila de reprodução, mas foi ai que eu percebi pra que os JSON "catalogo" serviam.

Demorei pra entender que meus dados foram organizados em "conteúdos" e "usuários" dentro dos JSON, eu estava sem saber como modelar os métodos por causa disso. Depois que você desenvolve o init e a primeira função fica tudo mais tranquilo.

Eu não estava entendendo a função do gabarito_publico.json e do consultas.json até que 






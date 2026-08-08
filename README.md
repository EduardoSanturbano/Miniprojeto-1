# Decisões de Modelagem

Criei a class Catalogo;
Modelei os métodos da fila de reprodução;
Desenvolvi o cli usando match case e as funções de cada caso;
Verifiquei os inputs durante o funcionamento do programa pra implementar no cli;
Modelei os outros métodos adaptando para tratar possíveis sujeiras;
Ajustei o cli pra tratar erros;


# Diário
Querido diário, o fato da classe Catalogo ter o C maiusculo me incomoda. O fato de João ter adiado o prazo me conforta.
Querido diário, fiquei muito feliz quando vi que vocês deram a class Catalogo pronta... Eu estava desenvolvendo ela com base na lógica, mas isso vai me ajudar muito.
Querido diário, eu não li em canto algum que era proibido escrever um diário!

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

# Dificuldades encontradas

Primeiro eu fiquei sem entender em qual dos arquivos (catalogo, cli e main) eu escrevia as classes do class Catalogo, mas interpretando com calma e sem medo de ter que programar vários arquivos eu percebi que é na propria catalogo.py.

Desenvolvendo a parte da fila de reprodução eu percebi que o código exemplo site retorna strings junto com as request, eu acho que isso seja implementado no cli porque nem todos os metodos retornam strings.

Como assim a Catalogo "carrega o JSON" e "constroi os índices no init"? Acredito que vou descobrir + pra frente.

Ainda não entendi em que parte do processo os 4 json entram.

To confuso, a função de listar usuários é só um print dos 33 ou eu tenho que de alguma forma coletar os dados e verificar quantos usuários são?







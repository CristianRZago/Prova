# Prova

## Introdução
### Ideia

Minha ideia foi criar um codigo python cheio de Fks(Chaves estrangeiras) para me desafiar e forçar a aprender python, porem com o decorrer do projeto fui percebendo
que ainda não era a hora de usar as FKs que era divertido programar em python.Já para a realização do projeto em si, foi criado algo bem abstrato, onde temos 3 funções
(preço final de um produto, calculadora e seu dono ligados e uma calculadora) e deixando espaço para a introdução para as FKs e novas funcionalidades.

### Motivo/Objetivos

Este projeto foi realizado com o proposito de cumprir os requerimentos que meu professor (Lucas venez) propos, sendo esses requerimentos: 
i) Defina o contexto do projeto e ao menos 3 funcionalidades descritas conforme o padrão de User Story (US) apresentado em https://www.scaledagileframework.com/story/. Cada US deve conter seu título, Critérios de Aceitação (CA) e Definition of Done (DoD);

ii) Desenvolva o modelo relacional do projeto, sendo que este deve conter ao menos 1 relacionamento 1:1, 3 relacionamentos 1:n e 2 relacionamentos n:n;

iii) Desenvolva o diagrama de classes UML correspondente ao modelo relacional; e

iv) Desenvolva o código Python com base no framework SQLALchemy para o mapeamento objeto-relacional.

O projeto deve ser entregue em um repositório público do github na sua conta pessoal. O projeto pode ter o título que desejar. O repositório deve conter um arquivo markdown denominado README.md descrevendo os itens i a iii e os códigos .py no diretório denominado orm dentro do repositório.

Desenvolva os diagramas utilizando a ferramenta StarUML (MER e Classes) e exporte as imagens e as insira no seu arquivo README.md.

### Conclusão

Após a realização deste projeto cheguei a conclusão que ainda tenho um longo caminho a ser percorrido nessa maravilhosa área de programação, onde tudo que aprendi até aqui é apenas a ponta de um grande iceberg e tenho que estudar cada vez mais para desbravar este grande desafio.


## Funções

1) CalcPrecoFinal<br>
2) Dono<br>
3) Calcular<br>

## User Story
1)<br>
como Pegando preço e desconto <br>
quero Valor final<br>
para que Informar o preço real<br>
2)<br>
como Juntando Pessoa e calculadora<br>
quero Identificar de quem é a calculadora<br>
para que Para caso alguem perca sua calculadora, ela esteja registrada<br>
3)<br>
como Pegando 2 numeros<br>
quero Resultado da conta que o usuario deseja<br>
para Satisfazer o usuario<br>

## Critérios de Aceitação
1)
dado o preço e o desconto<br>
quando realizar a conta<br>
então informar o usuario <br>
2)
dado a pessoa e a calculadora<br>
quando juuntar os dois<br>
então informar a união<br>
3)
dado os numeros<br>
quando realizar a conta<br>
então apresentar os resultados<br>

## Definition of Done
1.)
Cumprir os criterios de aceitação<br>
testes primarios<br>
checkin do codigo<br>
testes finais<br>
Aprovação do criador do código<br>

2.)
Cumprir os criterios de aceitação<br>
testes primarios<br>
checkin do codigo<br>
testes finais<br>
Aprovação do criador do código<br>

3.)
Cumprir os criterios de aceitação<br>
testes primarios<br>
checkin do codigo<br>
testes finais<br>
Aprovação do criador do código<br>

## Descrição do código
Antes de começarmos a falar do código, é importante você ter instalado as bibliotecas "mysql-connector-python" e "sqlalchemy", além de modificar a URL com base em seu banco de dados e criar a database orm.
Logo no começo do código nós importamos algumas funções das bibliotecas que instalamos para usarmos na criação das classes e ne ligação com o banco de dados, após isso
nós definimos a "URL", que é uma rota que vai acessar nosso banco de dados, e definimos "Base", onde base recebe declarative_base() (para ficar mais facil de chamar
ela na criação das tables), após isso nós criamos as nossas tables, onde elas tem como parâmetro "Base", Continuando, nesta parte do código nós criamos e coletamos os
atributos que iremos enviar posteriormente para o banco de dados atravéz de simples váriaveis e if elses, ajudando o usuario a identificar cada atributo atravéz de
prints pelo comando "input()". Após a coleta dessas váriaveis é criada uma "engine" que vai ter como parametro a "URL", que vai possibilitar ele a entrar no banco de
dados pela rota da URL, após isso, todas a tables do orm são deletadas e recriadas, continuando, é criado uma "Session", que vai receber um "sessionmaker" (ou criador
de sessão) false, que vai entrar e sair do banco de dados inserindo a primeira atualização de cada dado (se tiver duas pessoas, só a primeira irá entrar), e
finalizando o código, nós temos o Session.begin, que irá definir o começo da sessão, e dentro dele foi inserido as informações (com a ajuda do session.add) que foram pedidas anteriormente, e no fim do Session.begin todas as informações entrão dentro do banco de dados.


## Imagens

![Final](https://user-images.githubusercontent.com/102041250/193493979-3633c546-319b-4b99-9115-2181e409e912.png)

![MER](https://user-images.githubusercontent.com/102041250/193493993-7d985f75-d51e-4d91-a3a0-9f0c6e69dbe3.png)



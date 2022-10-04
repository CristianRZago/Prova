## Prova

# Introdução
Este projeto foi realizado com o intuito de cumprir os requerimentos que meu professor (Lucas venez) propos, sendo esses requerimentos: 
i) Defina o contexto do projeto e ao menos 3 funcionalidades descritas conforme o padrão de User Story (US) apresentado em https://www.scaledagileframework.com/story/. Cada US deve conter seu título, Critérios de Aceitação (CA) e Definition of Done (DoD);

ii) Desenvolva o modelo relacional do projeto, sendo que este deve conter ao menos 1 relacionamento 1:1, 3 relacionamentos 1:n e 2 relacionamentos n:n;

iii) Desenvolva o diagrama de classes UML correspondente ao modelo relacional; e

iv) Desenvolva o código Python com base no framework SQLALchemy para o mapeamento objeto-relacional.

O projeto deve ser entregue em um repositório público do github na sua conta pessoal. O projeto pode ter o título que desejar. O repositório deve conter um arquivo markdown denominado README.md descrevendo os itens i a iii e os códigos .py no diretório denominado orm dentro do repositório.

Desenvolva os diagramas utilizando a ferramenta StarUML (MER e Classes) e exporte as imagens e as insira no seu arquivo README.md.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Minha ideia foi criar um codigo python cheio de Fks(Chaves estrangeiras) para me desafiar e forçar a aprender python, com o decorrer do projeto fui percebendo que é divertido programar em python, já para o projeto em si, tentei criar algo bem abstrato, onde temos 3 funções (preço final de um produto, calculadora e seu dono ligados e uma calculadora).

Com a realização desta prova acredito que melhorei bastente em python e reaprendi muita coisa sobre sql e MER, como já dizia um filosófo, daqui pra frente é só pra tras (mas espero que daqui pra frente tudo melhore)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Funções

1) CalcPrecoFinal
2) Dono
3) Calcular

# User Story
1)
como Pegando preço e desconto
quero Valor final
para que Informar o preço real
2)
como Juntando Pessoa e calculadora
quero Identificar de quem é a calculadora
para que Para caso alguem perca sua calculadora, ela esteja registrada
3)
como Pegando 2 numeros
quero Resultado da conta que o usuario deseja
para Satisfazer o usuario

Critérios de Aceitação
1)
dado o preço e o desconto
quando realizar a conta
então informar o usuario
2)
dado a pessoa e a calculadora
quando juuntar os dois
então informar a união
3)
dado os numeros
quando realizar a conta
então apresentar os resultados

Definition of Done
1)
testes primerios
checkin do codigo
testes finais
Cumprir os criterios de aceitação
Apresentação do preço final para o usuario

2)
checkin do codigo
Cumprir os criterios de aceitação
Apresentação da união para o usuario
3)
checkin do codigo
Cumprir os criterios de aceitação
Apresentação do resultado para o usuario



![Final](https://user-images.githubusercontent.com/102041250/193493979-3633c546-319b-4b99-9115-2181e409e912.png)

![MER](https://user-images.githubusercontent.com/102041250/193493993-7d985f75-d51e-4d91-a3a0-9f0c6e69dbe3.png)



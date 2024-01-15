### Exercícios de nivelamento para vaga Desenvolvedor Pleno/Sênior Python no grupo SEB

## Para execução conforme esperado, é preciso que hajam as permissões de escrita disponíveis, pois foram implementadas funções de gerar uma "saída" da execução.
## Sendo 1 arquivo Excel com os dados raspados no Exercício 1 e Screenshot para o Exercício 2, ambos salvos em pastas específicas para cada, dentro do projeto.

## 1. Acesso ao Site de Vagas (https://gruposeb.gupy.io/):
  - Objetivo: Coletar informações sobre as vagas disponíveis (Cargo, Localidade, Efetividade).

## Tal exercício foi feito usando 
+ BeautifulSoup 
+ numpy
+ openpyxl
+ requests
+ OS 
+ datetime

As bibliotecas foram usadas para fazer o webscrapping guardar os dados em um array assim inputando todos em um excel
que é salvo em uma pasta criada dentro do projeto, para conter os xlsx com os resultados da raspagem. 
Todos os arquivos são guardados junto a data e hora do salvamento, para melhor controle.



## 2. Acesso ao Formulário (https://forms.office.com/r/zfipx2RFsY):
 - Objetivo: Preencher as informações e selecionar o flag apropriado.

## Tal Exercício foi feito usando 
+ Selenium
+ ChromeDriverManager
+ datetime
+ OS

As bibliotecas foram usadas para acessar o site e fazer as ações solicitadas, para as interações, criei assim como em meus projetos atuais, um arquivo de "web_functions" tal arquivo, que é sempre atualizado conforme necessário, tem as ações comumente usadas no decorrer 
da execução do código, deixando o código mais organizado e otimizando tempo de desenvolvimento;

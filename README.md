# climatologia
Você se candidatou para participar do processo seletivo - posição Analista - Desenvolvedor Python.
Gostaríamos de compartilhar a primeira etapa, um desafio J e ai, topa?
Desafio – Extração de dados site Clima Tempo
Utilizando a linguagem Python e as bibliotecas Selenium e Beautiful Soup, desenvolva um software que faça a extração de alguns dados do site Clima Tempo.
https://www.climatempo.com.br/climatologia/2/santos-sp
Extração de pelo menos 100 cidades, em ordem começando pelo estado do Acre, contendo com as seguintes informações:

·         Cidade
·         Estado
·         Mês
·         Minima (°C)
·         Máxima (°C)
·         Precipitação (mm)
# Minha Parte

Desafio J ? Não entendi. Mas vamos lá. Nunca usei Selenium, e não ficou claro como deveria ser utilizado, mas o usei para clicar e obter valores do popup estado cidade que abre. Uma maneira de resolver o problema seria fazer o Selenium clicar no botão com o estado e cidade selecionado, mas isso seria muito demorado, então analisei que seria possível criar a url para a cidade estado, a mesma tem este formato:

```
link = 'https://www.climatempo.com.br/climatologia/2/santos-sp'
Que pode ser resumida: link = 'https://www.climatempo.com.br/climatologia/{}/{}-{}'.format(id,city,state)
```

Esta valores podem ser obtidos via selenium e armazenados em alguns dicionários.

Assim no arquivo seleniumget_state_city.py eu obtenho todos os dados necessários, eu os salvei no arquivo output.py para observar.

Agora usando o BS4 com o arquivo selenium_dicio.py eu leio a url e salvo as informações. não ficou claro este mês, pois existe todos os meses na pagina, então salvei tudo.
Também não foi falado o formato de saída, então fiz uma lista de dicionários com os valores de Cidade, Estado, Mês, MIN, MAX, Precipitação.

Enfim como funciona.

# Como testar
## Primeiro
Rodar o arquivo seleniumget_state_city.py obter os valores de output salvar no arquivo output.py. Esta etapa não automatizei, pois não sei se é foco do desafio

## Segundo

Rodar o arquivo selenium_dicios.py e ele salvará os dados em forma de lista na variável lista que fica em memoria, pronta para ser enviada para algum lugar.

Coloquei um limitador para 100 links, mas testei com todos os links e funciona, só precisa tomar cuidado para não estourar a memoria.

# The-Star-Wars-API

O que esse repositório faz?

1. Coleta de Dados: Usaremos a API do SWAPI para coletar dados sobre planetas, pessoas e starships.
2. Armazenamento em Banco de Dados: Armazenaremos os dados coletados em um banco de dados acessível via Python, o SQLite.
3. Criação de uma API HTTP(S): Utilizaremos um framework, o Flask, para criar endpoints que disponibilizem os dados


Certifique-se de que você tem o Python, as libraries requests e Flask instaladas. 

Para instalar Flask, use o seguinte comando:
```
pip install Flask
```

Para instalar requests, use o seguinte comando:
```
pip install requests
```

## Na primeira execução, rode a ingestão dos dados da api com o comando:
```
python data_ingestor.py
```

## Se quiser testar se a ingestão de dados via API funcionou, rode o teste disponível:
```
python test.py
```

## Execute o script:
```
python sw_api.py
```

## Consulte a API:

A API estará disponível nos endpoints abaixo para obter alguns dados interessantes sobre o mundo Star Wars:

1. 3 planetas mais quentes do universo Star Wars: http://127.0.0.1:5000/hottest_planet

2. 5 personagens que mais aparecem nos filmes Star Wars: http://127.0.0.1:5000/appears_most

3. 3 naves mais rápidas do universo Star Wars: http://127.0.0.1:5000/fastest_ships

4. 3 armas/naves mais poderosas* do universo Star Wars: http://127.0.0.1:5000/powerful_weapon


*Aqui as mais poderosas, são as mais caras considerando o campo cost_in_credits da api.

# The-Star-Wars-API

O que esse repositório faz?

1. Coleta de Dados: Usaremos a API do SWAPI para coletar dados sobre planetas, pessoas e starships.
2. Armazenamento em Banco de Dados: Armazenaremos os dados coletados em um banco de dados acessível via Python, o SQLite.
3. Criação de uma API HTTP(S): Utilizaremos um framework, o Flask, para criar endpoints que disponibilizem os dados


Certifique-se de que você tem o Python e Flask instalados. Para instalar Flask, use o seguinte comando:

```
pip install Flask
```
## Na primeira execução, rode a ingestão dos dados da api com o comando:
```
python data_ingestor.py
```

## Execute o script:

```
python sw_api.py
```

## Teste a API:

A API estará disponível em http://127.0.0.1:5000/. Você pode acessar os endpoints abaixo para obter alguns dados interessantes:

1. http://127.0.0.1:5000/hottest_planet

2. http://127.0.0.1:5000/appears_most

3. http://127.0.0.1:5000/fastest_ships

4. http://127.0.0.1:5000/powerful_weapon

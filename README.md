# Acessando AwesomeAPI utilizando RASA


[![N|Solid](https://1805791138-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/spaces%2F-LDDJfbHDy3v965nUzNO%2Favatar.png?generation=1527103896608667&alt=media)](https://docs.awesomeapi.com.br/api-de-moedas) [![Build Status](https://goodhere.org/static/e4cde8fd927f0fae9e434da6fa030752/91bed/mfehiczg1xpug7tkkeue.png)](https://rasa.com/)

Rasa é uma plataforma de IA, especialista em conversação. Por meio dela, vamos simular uma conversação sobre taxa de conversão de valores de moedas. Acessando a AwesomeAPI, será possivel realizar esse trabalho.

## Descrição

- Quando iniciamos o projeto, um chatbot é acessado, com a função de coletar alguns dados.
- Depois dos dados coletados, o chatbot retorna a consulta feita na API em formato JSON.


## Instalação

Requer Python 3.8.13 e RASA 3 instalados na máquina.
Links com tutorial de instalação:
| Plugin | Links |
| ------ | ------ |
| Python | [https://www.python.org/downloads/][PlDb] |
| RASA | [https://www.youtube.com/watch?v=tXiYJM2vGJk&t=288s][PlGh] |

Faça o clone do projeto:

```sh
git clone https://github.com/suelen-prs/chatbot_awesome_api.git
cd chatbot_awesome_api
```
Inicie o RASA dentro da pasta

```sh
rasa init
```
Treine seu chatbot

```sh
rasa shell
```
Inicie a conversasção

```sh
rasa shell
```
Se precisar reiniciar a conversação

```sh
/restart
```
Termine a conversação

```sh
/stop
```

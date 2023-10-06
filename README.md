# setrem-iot-middleware
Este repositório representa o código-fonte do MIDDLEWARE da automação.
- Broker MQTT
- Aplicação Python que escuta as mensagens de um tópico MQTT e envia via API.

## Preparando o meu ambiente
- Instalando o pyenv para Windows: https://github.com/pyenv-win/pyenv-win

- Instalando versão 3.11.0 do Python via pyenv:
```sh
pyenv install 3.11.0
```

- Configurando a versão 3.11.0 como a default:
```sh
pyenv global 3.11.0
```

## Testing
Gerenciamento dos pacotes os pacotes Python via [Poetry](https://python-poetry.org/).

```sh
poetry install
poetry shell
python app.py
```

## Production
- Iniciando o middleware
```sh
docker compose up --build
```

## Ports
```yaml
management: 15672
qmqp: 5672
mqtt: 1883
```

## Material de apoio:
- [Referência de projeto IoT utilizando RabbitMQ](https://funprojects.blog/2018/12/07/rabbitmq-for-iot/)
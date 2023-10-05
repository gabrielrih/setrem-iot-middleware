# setrem-iot-middlware

## Managing Python version
- [pyenv for Windows](https://github.com/pyenv-win/pyenv-win)

## Installing Python versions
Using pyenv.

```sh]
pyenv install 3.10.0
pyenv install 3.11.0
```

Setting a Python version via pyenv:
```sh
pyenv global 3.11.0
```


## Running on real environment
```sh
docker compose up --build
```

## Endpoints
```sh
coap://192.168.155.182/whoami
coap://192.168.155.182/humidity
```

## Managing Python packages
- Poetry: https://python-poetry.org/

## Testing
```sh
poetry install
poetry shell
python app.py
```

FROM python:3.8

COPY CryptoBot/main.py /CryptoBot/
COPY CryptoBot/assets.py /CryptoBot/
COPY CryptoBot/exchanges.py /CryptoBot/
COPY CryptoBot/elon.py /CryptoBot/

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

WORKDIR /CryptoBot

CMD ["python", "main.py"]
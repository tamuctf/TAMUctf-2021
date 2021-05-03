FROM debian

RUN apt-get update -y; apt-get install socat python3 -y
COPY game.py /pwn/game.py
COPY flag.txt /pwn/flag.txt

WORKDIR /pwn

EXPOSE 9397

ENTRYPOINT ["sh", "-c", "exec socat -s TCP-LISTEN:9397,reuseaddr,fork EXEC:'python3 /pwn/game.py',stderr"]

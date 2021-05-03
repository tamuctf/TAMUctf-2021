FROM alpine as build

RUN apk add --update alpine-sdk
ADD lottery.c /tmp/lottery.c
ADD Makefile /tmp/Makefile
RUN cd /tmp/; make all

FROM debian

RUN apt-get update -y; apt-get install socat -y
COPY --from=build /tmp/lottery /pwn/lottery
COPY flag.txt /pwn/flag.txt
ADD solve.py /pwn/solve.py
WORKDIR /pwn

EXPOSE 5906

ENTRYPOINT ["sh", "-c", "exec socat -s TCP-LISTEN:5906,reuseaddr,fork EXEC:/pwn/lottery,stderr"]

FROM debian:bullseye-slim as build

RUN apt-get update -y; apt-get install build-essential -y
ADD pancake.c /tmp/pancake.c
ADD Makefile /tmp/Makefile
RUN cd /tmp/; make all

FROM debian:bullseye-slim

RUN apt-get update -y;apt-get install socat -y

COPY --from=build /tmp/pancake /pwn/pancake
WORKDIR /pwn

ADD flag.txt .

EXPOSE 3220

ENTRYPOINT ["sh", "-c", "exec socat TCP-LISTEN:3220,reuseaddr,fork EXEC:/pwn/pancake,stderr"]

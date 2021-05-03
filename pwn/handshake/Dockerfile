FROM debian:bullseye-slim as build

RUN apt-get update -y
RUN apt-get install build-essential gcc-multilib  -y
ADD handshake.c /tmp/handshake.c
RUN cd /tmp/; gcc handshake.c -no-pie -fno-stack-protector -m32 -o handshake

FROM debian

RUN dpkg --add-architecture i386
RUN apt-get update -y
RUN apt-get install socat libc6-i686 -y

COPY --from=build /tmp/handshake /pwn/handshake
COPY flag.txt /pwn/flag.txt
COPY flag.txt /pwn/flag.txt
WORKDIR /pwn

EXPOSE 4212

ENTRYPOINT ["sh", "-c", "exec socat TCP-LISTEN:4212,reuseaddr,fork EXEC:/pwn/handshake,stderr"]

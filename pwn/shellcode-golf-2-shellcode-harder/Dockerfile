FROM debian as build

RUN apt-get update -y; apt-get install build-essential -y
ADD shellcode-golf.c /tmp/shellcode-golf.c
ADD Makefile /tmp/Makefile
RUN cd /tmp/; make all

FROM debian

RUN apt-get update -y; apt-get install socat -y
COPY --from=build /tmp/shellcode-golf /pwn/shellcode-golf
COPY flag.txt /pwn/flag.txt
WORKDIR /pwn

EXPOSE 5321

ENTRYPOINT ["sh", "-c", "exec socat -s TCP-LISTEN:5320,reuseaddr,fork EXEC:/pwn/shellcode-golf,stderr"]

FROM debian as build

RUN apt-get update -y; apt-get install build-essential -y
ADD calculator.c /tmp/calculator.c
ADD Makefile /tmp/Makefile
RUN cd /tmp/; make all

FROM debian

RUN apt-get update -y; apt-get install socat -y
COPY --from=build /tmp/calculator /pwn/calculator
COPY flag.txt /pwn/flag.txt
WORKDIR /pwn

EXPOSE 6319

ENTRYPOINT ["sh", "-c", "exec socat -s TCP-LISTEN:6319,reuseaddr,fork EXEC:/pwn/calculator,stderr"]

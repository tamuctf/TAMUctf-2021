FROM debian:bullseye-slim as build

RUN apt-get update -y; apt-get install build-essential -y
ADD leaky.c /tmp/leaky.c
ADD flag_check.c /tmp/flag_check.c
ADD Makefile /tmp/Makefile
RUN cd /tmp/; make all

FROM debian:bullseye-slim

RUN apt-get update -y;apt-get install socat -y

COPY --from=build /tmp/leaky /pwn/leaky
COPY --from=build /tmp/flag_check.o /pwn/flag_check.o
WORKDIR /pwn

EXPOSE 8374

ENTRYPOINT ["sh", "-c", "exec socat TCP-LISTEN:8374,reuseaddr,fork EXEC:/pwn/leaky,stderr"]

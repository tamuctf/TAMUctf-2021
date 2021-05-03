FROM alpine as build

RUN apk --no-cache add alpine-sdk

WORKDIR /opt/build
ADD Makefile /opt/build/Makefile
ADD nx-oopsie.c /opt/build/nx-oopsie.c

RUN make

FROM alpine

RUN apk --no-cache add socat

EXPOSE 7234

COPY --from=build /opt/build/nx-oopsie /usr/bin/nx-oopsie
ADD flag.txt /root/flag.txt

WORKDIR /root

ENTRYPOINT ["socat", "TCP-LISTEN:7234,reuseaddr,fork", "EXEC:/usr/bin/nx-oopsie,stderr"]

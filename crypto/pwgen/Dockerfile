FROM rust:alpine

RUN apk add --update socat

COPY . /chall/.
WORKDIR /chall

RUN cargo build --release
EXPOSE 4662

ENTRYPOINT ["sh", "-c", "exec socat TCP-LISTEN:4662,reuseaddr,fork EXEC:/chall/target/release/check,stderr"]
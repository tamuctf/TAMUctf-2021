FROM rust

RUN apt-get update -y
RUN apt-get install -y seccomp libseccomp-dev libpython3.7-dev socat

COPY restricted_python /pwn/restricted_python
COPY flag.txt /pwn/flag.txt
WORKDIR /pwn

RUN cd restricted_python && cargo build --release
EXPOSE 7234

ENTRYPOINT ["sh", "-c", "exec socat TCP-LISTEN:7234,reuseaddr,fork EXEC:/pwn/restricted_python/target/release/restricted_python,stderr"]

FROM rust as build

ADD src /opt/delfi/src
ADD Cargo.toml /opt/delfi/Cargo.toml

WORKDIR /opt/delfi

RUN cargo build --release

FROM ubuntu

RUN adduser --disabled-password --gecos "" delfi
WORKDIR /home/delfi

COPY --from=build /opt/delfi/target/release/delfi /home/delfi/bin/delfi
COPY --from=build /opt/delfi/target/release/get_flag /usr/sbin/get_flag

COPY flag /root/flag

RUN chmod 600 /root/flag
RUN chmod u+s /usr/sbin/get_flag

EXPOSE 3030

ENTRYPOINT ["su", "delfi", "-c", "/home/delfi/bin/delfi"]

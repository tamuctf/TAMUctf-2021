FROM rust as build

COPY Cargo.toml /tmp/
RUN mkdir /tmp/src
RUN touch /tmp/src/main.rs

WORKDIR /tmp
RUN cargo build --release || exit 0

COPY src/main.rs /tmp/src/main.rs

RUN cargo build --release

# I'm so sorry
FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
RUN cd /tmp; \
    apt update; \
    apt -y install libssl-dev wget; \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb; \
    apt update; \
    apt -y install ./google-chrome-stable_current_amd64.deb

COPY --from=build /tmp/target/release/chrome-capture /usr/local/bin/chrome-capture

EXPOSE 9000

ENTRYPOINT ["timeout","10m", "chrome-capture"]

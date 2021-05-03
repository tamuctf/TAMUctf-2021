FROM rust as build

COPY Cargo.toml /tmp/
RUN mkdir /tmp/src
RUN touch /tmp/src/main.rs

WORKDIR /tmp
RUN cargo build --release || exit 0

COPY src/main.rs /tmp/src/main.rs
COPY src/index.html /tmp/src/index.html

RUN cargo build --release

# I'm so sorry
FROM ubuntu

RUN apt update; apt -y install libssl-dev

COPY --from=build /tmp/target/release/chrome-handler /usr/local/bin/chrome-handler

EXPOSE 8000

ENTRYPOINT ["chrome-handler"]
FROM ubuntu:focal

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y socat qemu-system-misc qemu-user crossbuild-essential-riscv64

EXPOSE 7238

COPY meet-me-under-the-arch.riscv64 /usr/bin/meet-me-under-the-arch

WORKDIR /root

ENTRYPOINT ["socat", "-d", "-d", "TCP-LISTEN:7238,reuseaddr,fork", "EXEC:qemu-riscv64 -L /usr/riscv64-linux-gnu /usr/bin/meet-me-under-the-arch,stderr"]

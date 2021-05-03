FROM debian:buster-slim

EXPOSE 5309

RUN printf "\n\
deb-src http://deb.debian.org/debian buster main\n\
deb-src http://security.debian.org/debian-security buster/updates main\n\
deb-src http://deb.debian.org/debian buster-updates main" >> /etc/apt/sources.list

RUN apt update && apt -y build-dep gdb && apt -y install curl tar libmpc-dev libbabeltrace-dev socat

RUN mkdir -p /opt/gdb && cd /opt/gdb && \
    curl "http://mirrors.kernel.org/sourceware/gdb/releases/gdb-10.1.tar.xz" | tar xvJ
RUN mkdir -p /opt/gdb/gdb-10.1/build && cd /opt/gdb/gdb-10.1/build && \
    ../configure \
        --host=x86_64-linux-gnu --target=x86_64-linux-gnu \
        --with-auto-load-dir=/ \
        --with-auto-load-safe-path=/ \
        --with-expat \
        --with-gdb-datadir=/usr/share/gdb \
        --with-jit-reader-dir=/usr/lib/gdb \
        --without-libunwind-ia64 \
        --with-lzma \
        --with-babeltrace \
        --without-intel-pt \
        --with-mpfr \
        --without-xxhash \
        --with-python=/usr \
        --without-guile \
        --disable-source-highlight \
        --with-separate-debug-dir=/usr/lib/debug \
        --with-system-gdbinit=/etc/gdb/gdbinit

RUN cd /opt/gdb/gdb-10.1/build && \
    make -j$(nproc) && \
    strip /opt/gdb/gdb-10.1/build/gdb/gdb && \
    make install

RUN rm -rf /opt/gdb

COPY runloop.sh /opt/runloop.sh
RUN chmod +x /opt/runloop.sh

COPY flag.txt /root/flag.txt

CMD exec socat -d -d tcp-l:5309,reuseaddr,fork exec:/opt/runloop.sh,stderr

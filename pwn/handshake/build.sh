#!/bin/sh
docker build -t gcc:handshake -f Dockerfile.build .
docker run --user $(id -u):$(id -g) --rm -ti -v $(pwd):/opt/build gcc:handshake handshake.c -no-pie -fno-stack-protector -m32 -o handshake
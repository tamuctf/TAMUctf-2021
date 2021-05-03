CC := clang-11
CFLAGS := 
CONTAINER := meet-me-under-the-arch

all: meet-me-under-the-arch

clean: .PHONY
	rm -f meet-me-under-the-arch.aarch64 meet-me-under-the-arch.riscv64

meet-me-under-the-arch: meet-me-under-the-arch.aarch64 meet-me-under-the-arch.riscv64

meet-me-under-the-arch.aarch64: meet-me-under-the-arch.c
	$(CC) -target aarch64-linux-gnu $(CFLAGS) $^ -o $@

meet-me-under-the-arch.riscv64: meet-me-under-the-arch.c
	$(CC) -target riscv64-linux-gnu -L /usr/riscv64-linux-gnu/lib/ $(CFLAGS) $^ -o $@

docker: Dockerfile meet-me-under-the-arch.riscv64
	docker build -t $(CONTAINER) .

run: docker
	docker run --rm -ti -p 7238:7238 --name meet-me-under-the-arch meet-me-under-the-arch

.PHONY:
.SUFFIXES:

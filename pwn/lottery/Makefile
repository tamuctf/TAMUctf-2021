CC := $(or $(CC),gcc)
CFLAGS := -O2 -static -no-pie -fno-stack-protector
CONTAINER := lottery

all: lottery

clean: .PHONY
	rm -f lottery

lottery: lottery.c
	$(CC) $(CFLAGS) $^ -o $@

docker: Dockerfile lottery
	docker build -t $(CONTAINER) .

run: docker
	docker run --rm -ti --name lottery -p 5906:5906 lottery

extract: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/pwn/lottery - | tar xv lottery
	docker rm -v $(id)

.PHONY:

CC := $(or $(CC),gcc)
CFLAGS := -fno-stack-protector -no-pie
CONTAINER := leaky

all: leaky flag_check

clean: .PHONY
	rm -f leaky flag_check.o

leaky: leaky.c
	$(CC) $(CFLAGS) $^ -o $@

flag_check: flag_check.c
	$(CC) -fno-asynchronous-unwind-tables -s -c $^ -o $@.o

docker: Dockerfile leaky.c flag_check.c
	docker build -t $(CONTAINER) .

run: docker
	docker run --rm -ti --name $(CONTAINER) $(CONTAINER)

run_detached: docker
	docker run --rm -d -p 8374:8374 --name $(CONTAINER) $(CONTAINER)


extract: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/pwn/. - | tar xv
	docker rm -v $(id)

.PHONY:
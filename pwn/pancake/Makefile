CC := $(or $(CC),gcc)
CFLAGS := 
CONTAINER := pancake

all: pancake

clean: .PHONY
	rm -f leaky

leaky: leaky.c
	$(CC) $(CFLAGS) $^ -o $@

docker: Dockerfile pancake.c
	docker build -t $(CONTAINER) .

run: docker
	docker run --rm -ti --name $(CONTAINER) $(CONTAINER)

run_detached: docker
	docker run --rm -d -p 3220:3220 --name $(CONTAINER) $(CONTAINER)


extract: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/pwn/. - | tar xv
	docker rm -v $(id)

.PHONY:

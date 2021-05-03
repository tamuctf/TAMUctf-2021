CC := $(or $(CC),gcc)
CFLAGS := -fno-stack-protector -z execstack
CONTAINER := nx-oopsie

all: nx-oopsie

clean: .PHONY
	rm -f nx-oopsie

nx-oopsie: nx-oopsie.c
	$(CC) $(CFLAGS) $^ -o $@

docker: Dockerfile nx-oopsie.c
	docker build -t $(CONTAINER) .

run: docker
	docker run --rm -ti --name nx-oopsie nx-oopsie

extract: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/usr/bin/nx-oopsie - | tar xv nx-oopsie
	docker rm -v $(id)

.PHONY:

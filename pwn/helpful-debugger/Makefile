CC := $(or $(CC),gcc)
CFLAGS := -O2 -static -no-pie -fno-stack-protector
CONTAINER := helpful-debugger

all: gdb

clean: .PHONY
	rm -f gdb

docker: Dockerfile
	docker build -t $(CONTAINER) .

run: docker
	docker run --rm -ti --name helpful-debugger -p 5309:5309 helpful-debugger

gdb: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/usr/local/bin/gdb - | tar xv gdb
	docker rm -v $(id)

.PHONY:

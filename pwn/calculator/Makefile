CC := $(or $(CC),gcc)
CFLAGS := 
CONTAINER := calculator

all: calculator

clean: .PHONY
	rm -f calculator

calculator: calculator.c
	$(CC) $(CFLAGS) $^ -o $@

docker: Dockerfile
	docker build -t $(CONTAINER) .

run: docker
	docker run -d --read-only --restart=always --name calculator -p 6319:6319 calculator

extract: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/pwn/calculator - | tar xv calculator
	docker rm -v $(id)

.PHONY:

CC := $(or $(CC),gcc)
CFLAGS := 
CONTAINER := shellcode-golf-2

all: shellcode-golf

clean: .PHONY
	rm -f shellcode-golf

shellcode-golf: shellcode-golf.c
	$(CC) $(CFLAGS) $^ -o $@

docker: Dockerfile shellcode-golf
	docker build -t $(CONTAINER) .

run: docker
	docker run -d --read-only --restart=always --name shellcode-golf -p 5320:5320 shellcode-golf-2

extract: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/pwn/shellcode-golf - | tar xv shellcode-golf
	docker rm -v $(id)

.PHONY:

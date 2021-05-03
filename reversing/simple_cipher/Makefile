CC := $(or $(CC),gcc)
all: simple_cipher

clean: .PHONY
	rm -f simple_cipher

simple_cipher: simple_cipher.c
	$(CC) $(CFLAGS) $^ -o $@

.PHONY:

CC := ubicom32-linux-uclibc-gcc
OBJDUMP := ubicom32-linux-uclibc-objdump
CFLAGS := -fPIC -shared -O0
CONTAINER := check_flag.so

all: check_flag.so

distclean: .PHONY clean
	rm -rf constraintgen/venv

clean: .PHONY
	rm -f check_flag.*

constraintgen/venv:
	virtualenv --python $(shell which python3.8) constraintgen/venv
	bash -c "source constraintgen/venv/bin/activate; pip install z3-solver"

check_flag.c: constraintgen/venv constraintgen/main.py
	bash -c "source constraintgen/venv/bin/activate; python constraintgen/main.py"

check_flag.so: check_flag.c
	$(CC) $(CFLAGS) $^ -o $@

check_flag.dump: check_flag.so
	$(OBJDUMP) -d $^ > $@

.PHONY:

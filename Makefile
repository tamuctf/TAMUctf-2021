INSTANCES ?= 0
DIRS := $(shell find . -name problem.json -printf "%h\n")

install: $(addprefix install_,$(DIRS))

$(addprefix install_,$(DIRS)): install_%: %
	sudo shell_manager install $<

reinstall: $(addprefix reinstall_,$(DIRS))

$(addprefix reinstall_,$(DIRS)): reinstall_%: %
	sudo shell_manager install --reinstall $<

deploy: $(addprefix deploy_,$(DIRS))
	sudo service xinetd restart

$(addprefix deploy_,$(DIRS)): deploy_%: %
	sudo shell_manager deploy -n $(INSTANCES) -nr $(shell sudo shell_manager status | grep "$(shell jq -r .name $</problem.json)" | cut -d'(' -f 2 | cut -d')' -f 1)

test: $(addprefix test_,$(DIRS))
	sudo service xinetd restart

$(addprefix test_,$(DIRS)): test_%: %
	sudo shell_manager deploy -n $(INSTANCES) -d -nr $(shell sudo shell_manager status | grep "$(shell jq -r .name $</problem.json)" | cut -d'(' -f 2 | cut -d')' -f 1)

status:
	sudo shell_manager status

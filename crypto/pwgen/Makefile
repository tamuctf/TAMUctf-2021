CONTAINER := pwgen


clean: .PHONY
	rm -f pwgen check


docker: Dockerfile flag.txt password src
	docker build -t $(CONTAINER) .

run: docker
	docker run -d -p 4662:4662 --name $(CONTAINER) $(CONTAINER)


extract: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/chall/. - | tar xv
	docker rm -v $(id)

.PHONY:
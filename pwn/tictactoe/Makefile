CONTAINER := tictactoe


docker: Dockerfile
	docker build -t $(CONTAINER) .

run: docker
	docker run -d --read-only --restart=always --name tictactoe -p 9397:9397 tictactoe

.PHONY:

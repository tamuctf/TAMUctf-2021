# FROM postgres:13

FROM debian:buster-slim




# Move all items from directory to docker
RUN mkdir /opt/challenge

RUN apt-get -y update && apt-get -y install wget

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'; \
	wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -; \
	apt update -y; \
	apt install postgresql -y;


USER postgres
RUN mkdir /var/lib/postgresql/data
USER root
ENV PGDATA /var/lib/postgresql/data

# Golang
RUN wget https://golang.org/dl/go1.16.2.linux-amd64.tar.gz
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.2.linux-amd64.tar.gz
RUN /usr/local/go/bin/go mod init sequel
RUN /usr/local/go/bin/go get github.com/lib/pq
ADD ./ /opt/challenge
ADD templates/. /opt/challenge/.
RUN chmod +x /opt/challenge/start.sh

ENV POSTGRES_PASSWORD G@Wm5C84a%ey!%pmzRTRS%!!G$!v7zR4
EXPOSE 1337
WORKDIR /opt/challenge

RUN /usr/local/go/bin/go build

ENTRYPOINT ["/opt/challenge/start.sh"]
from python

RUN apt-get update -y \
    && apt-get install build-essential gdb openssh-server openssh-client sudo -y
RUN pip install flask pycryptodome flask-login Flask-Session

ADD flag.txt /root/flag.txt

RUN echo "ALL ALL = NOPASSWD: /usr/bin/gcore" >> /etc/sudoers

RUN mkdir /run/sshd

RUN cd /etc/ssh && ssh-keygen -A

RUN useradd -ms /bin/bash alice
RUN useradd -ms /bin/bash vault

USER alice

RUN mkdir ~/.ssh && ssh-keygen -q -t rsa -N '' -f "/home/alice/.ssh/id_rsa"


USER vault

COPY templates /home/vault/templates
ADD server.py /home/vault/server.py
ADD vault.sh /home/vault/vault.sh
RUN mkdir /home/vault/files

WORKDIR /home/vault/

USER root

RUN mkdir /root/.ssh && cp /home/alice/.ssh/id_rsa.pub /root/.ssh/authorized_keys

HEALTHCHECK --interval=1m --timeout=3s --retries=1 \
  CMD curl -f http://localhost:5000/ || exit 1

ADD start.sh /root/start.sh


EXPOSE 5000

ENTRYPOINT ["sh", "/root/start.sh"]

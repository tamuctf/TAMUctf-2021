#!/bin/sh

su - vault -c "/home/vault/vault.sh" &
su - alice -c 'eval "$(ssh-agent -s)"; ssh-add'

/usr/sbin/sshd -D
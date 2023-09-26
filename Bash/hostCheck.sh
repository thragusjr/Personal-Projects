#!/bin/bash

HOST="google.com"

# The -c flag used with "1" tells ping to send just one status
ping -c 1 $HOST

# "#?" contains the return code of the previously executed command

# A "0" exit status means a command executed successfully
# Any other exit status' indicates some sort of error

# If the exit status is 0, HOST is reachable
if [ "$?" -eq "0" ]
then
  echo "$HOST reachable."
# Else, the host is unreachable
else
  echo "$HOST unreachable."
fi

HOST="google.com"

ping -c 1 $HOST

# -ne flag means "not equal"
if [ "$?" -ne "0" ]
then
  echo "$HOST unreachable."
fi

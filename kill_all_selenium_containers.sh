#!/bin/sh

ps=$(docker ps --format '{{ .ID }} ')

for info in $ps; do
  docker kill $info
  docker rm $info
done

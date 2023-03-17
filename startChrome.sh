#!/bin/sh


docker run \
	--rm \
	-d \
	--name chrome \
	-p 4444:4444 \
	-p 7900:7900 \
	--shm-size="2g" \
	-e HTTP_PROXY="host.docker.internal:8888" \
	-e HTTPS_PROXY="host.docker.internal:8888" \
	-e NO_PROXY="localhost|127.*|172.*|10.250.*.*|10.249.*.*|10.190.*.*|10.191.*.*|*.balgroupit.com" \
	selenium/standalone-chrome:109.0

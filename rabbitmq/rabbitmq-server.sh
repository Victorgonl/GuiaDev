#!/bin/sh

sudo kill "$(sudo lsof -t -i :25672)"
sudo rabbitmq-server
#!/bin/bash

ping 151.101.194.167 | grep --line-buffered -Eo 'time=[^ ]*' | grep --line-buffered -Eo '[0-9]+\.[0-9]+' >> pings.dat





#!/bin/bash

cd /home/simulator
nohup socat tcp-l:5000,fork exec:./babyAnD &
export TERM=linux
export TERMINFO=/etc/terminfo
python ./attackmanager.py

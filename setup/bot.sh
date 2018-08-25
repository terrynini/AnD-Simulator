#!/bin/bash

cd /home/simulator
nohup socat tcp-l:5000,fork exec:./babyAnD &
export TERM=linux
export TERMINFO=/etc/terminfo

cd /
cp /opt/sim/setup/attack1.py ./
cp /opt/sim/setup/attackmanager.py ./
python ./attackmanager.py

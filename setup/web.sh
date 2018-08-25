#!/bin/bash

pip install Flask
cd /home/simulator

gcc -fno-stack-protector -no-pie /opt/sim/challenges/babyAnD/babyAnD.c -o babyAnD
chmod u+s babyAnD
cp babyAnD bot/
cp babyAnD player/

chmod a-w /home/simulator/player/flag
chown simulator:simulator /home/simulator/player/flag

chmod a-w /home/simulator/bot/flag
chown simulator:simulator /home/simulator/bot/flag
FLASK_DEBUG=1 python /opt/sim/server/game.py


#!/bin/bash

pip install Flask
cd /home/simulator

gcc -fno-stack-protector -no-pie /opt/sim/challenges/babyAnD/babyAnD.c -o babyAnD

chown simulator:simulator babyAnD
chmod u+s babyAnD
cp -p babyAnD bot/
cp -p babyAnD player/

echo -n "FLAG{`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1`}" > /home/simulator/player/flag
chown simulator:simulator /home/simulator/player/flag

echo -n "FLAG{`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1`}" > /home/simulator/bot/flag
chown simulator:simulator /home/simulator/bot/flag

python /opt/sim/server/game.py

#!/bin/bash
cd /home/simulator
socat tcp-l:5000,fork exec:./babyAnD 

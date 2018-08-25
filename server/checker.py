#! /usr/bin/env python
import curses
curses.setupterm()
from pwn import *
context.log_level = "ERROR"
def check(host, port):
    try:
        r = remote(host, port)
    except:
        print "FAIL"
        return 0

    out = ""
    with open("/opt/sim/server/check.input","r") as f:
        c_input = f.read().split("\n")
        
        try:
            out += r.recv()
            for i in c_input:
                r.sendline(i)
                out += r.recv()
                sleep(0.1)
        except:
            pass

    with open("/opt/sim/server/check.out","r") as f:
        temp = f.read()
        if out != temp:
            print "FAIL"
            return 0
    
    print "GOOD"
    return 0

if __name__ == "__main__":
    check("bot","5000")
    check("player","5000")

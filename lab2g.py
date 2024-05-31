#!/usr/bin/env python3

#Author: Vizi Vishnukumar patel
#Author ID: 120078225
#Date Created: 2024/05/31

import sys

timer = 3

if len(sys.argv) > 1:
	timer = int(sys.argv[1])
     
while timer > 0:
	print(timer)
	timer -= 1

print('blast off!')

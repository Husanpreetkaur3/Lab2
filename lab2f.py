#!/usr/bin/env python3
# Author: husanpreet kaur
# Author ID: husanpreet-kaur3
# Date Created: 2024/09/25

import sys

# Assign the first command-line argument to the timer
timer = int(sys.argv[1])  # Convert the argument to an integer

# While loop to count down
while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')

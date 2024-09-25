#!/usr/bin/env python3
# Author: husanpreet kaur
# Author ID: husanpreet-kaur3
# Date Created: 2024/09/25

import sys

# Check if there is a command-line argument, if not, set timer to 3
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Convert the argument to an integer
else:
    timer = 3  # Default value if no argument is provided

# While loop to count down
while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')

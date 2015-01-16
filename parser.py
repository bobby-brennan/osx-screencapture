#!/usr/bin/python

import os
import re

PID_WID_List = []
temp = os.popen('./GetWindowList 2>&1').read().strip().split('},')
for i in temp:
    match = re.search('kCGWindowOwnerPID = (\d+);', i)
    pid = match.group(1)
    match = re.search('kCGWindowNumber = (\d+);', i)
    wid = match.group(1)
    match = re.search('kCGWindowOwnerName = (.+);', i)
    owner = match.group(1)
    match = re.search('kCGWindowIsOnscreen = (\d+);', i)
    if match and owner == '"Google Chrome"':
      PID_WID_List.append((pid, wid))

print PID_WID_List

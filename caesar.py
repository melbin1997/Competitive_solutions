#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
new_s = ''
for i in s:
	if(i.isalpha()):
		if(i.isupper()):
			new_s += chr(ord('A') + (abs(ord('A')-((ord(i)+k))))%26)
		else:
			new_s += chr(ord('a') + (abs(ord('a')-((ord(i)+k))))%26)
	else:
		new_s += i

print new_s

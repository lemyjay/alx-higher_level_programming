#!/usr/bin/python3
result = ""
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        result += chr(i)
    else:
        result += chr(i).upper()
print(result, end="")

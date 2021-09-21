import os

printf = '''#include<stdio.h>\n\nint main()\n{printf("Hello, world!");\nreturn 0;}'''

with open("hello.c", mode="w") as file:
	file.write(printf)

os.system(f"gcc hello.c -o main")
os.system(".\\main")
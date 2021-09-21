import os

printf = '''#include<stdio.h>\n#include<stdlib.h>\nint main()\n{printf("\\nHello, world!\\n\\n");\nsystem("pause");\nreturn 0;}'''

with open("hello.c", mode="w") as file:
	file.write(printf)

os.system(f"gcc hello.c -o main")
os.system(".\\main")
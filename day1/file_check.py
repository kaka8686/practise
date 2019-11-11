"""

Version: 0.1
Author: Spike

"""

import platform

platform_name = platform.system()
file_path = "./files/pai.txt"
full_line = ""

try:
    with open(file_path,"r") as fo:
        print(fo.name)
        for line in fo.readlines():
            full_line += line.rstrip()
        full_line = full_line.replace(" ","")
        print(full_line)
except IOError:
    print("file not found")


# 猜生日是否在Pi内
# birthday = input("Enter your birthday,in the form mmddyy: ")
# if birthday in full_line:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")


# if(platform_name == "Windows"):
#     print("You're in Windows")
# elif(platform_name == "Darwin"):
#     print("You're in MacOS")


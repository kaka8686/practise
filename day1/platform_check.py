"""

Version: 0.1
Author: Spike

"""

import platform

platform_name = platform.system()

if(platform_name == "Windows"):
    print("You're in Windows")
elif(platform_name == "Darwin"):
    print("You're in MacOS")
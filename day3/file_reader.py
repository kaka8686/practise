import platform

def ListPlatform():
    print("--------Operation System----------------------")
    # Windows will be : (32bit, WindowsPE)
    # Linux will be : (32bit, ELF)
    print(platform.architecture())

    # Windows will be : Windows-XP-5.1.2600-SP3 or Windows-post2008Server-6.1.7600
    # Linux will be : Linux-2.6.18-128.el5-i686-with-redhat-5.3-FInal
    print(platform.platform())

    # Windows will be : Windows
    # Linux will be : Linux
    print(platform.system())

    print("-----------------Python Version----------------------")
    # Windows and Linux will be : 3.1.1 or 3.1.3
    print(platform.python_version())


def GetPlatform():
    sysstr = platform.system()
    if(sysstr == "Windows"):
        print("Call Windows Tasks")

file_path = '/Users/kevinz/workspace/python/practise/day3/text_files/pai.txt'



GetPlatform()



# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents)
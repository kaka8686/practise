import platform


def UsePlatform():
  sysstr = platform.system()
  if(sysstr =="Windows"):
    print ("Call Windows tasks")
  elif(sysstr == "Linux"):
    print ("Call Linux tasks")
  elif(sysstr == "Darwin"):
    print ("Call MacOS tasks")
  else:
    print ("Other System tasks")


def GetPath():
    sysstr = platform.system()
    if(sysstr == "Windows"):
        file_path = "D:\workspace\python\practise\day3\\text_file\pai.txt"
        return file_path
    elif(sysstr == "Darwin"):
        file_path = '/Users/kevinz/workspace/python/practise/day3/text_files/pai.txt'
        return file_path

# 根据系统类型还构建文件路径
file_path = GetPath()


# file_path = '/Users/kevinz/workspace/python/practise/day3/text_files/pai.txt'

with open(file_path) as file_object:
    # contents = file_object.read()
    # print(contents)
    lines = file_object.readlines()

pi_string = ' '
for line in lines:
    pi_string += line.strip()

# print(pi_string[:52] + "...")
# print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
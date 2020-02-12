import json

# 如果以前存储了用户名，就加载他
# 否则，就提示用户输入用户名并存储他

def get_stored_username():
    """ 如果存储了用户名，就获取他"""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """ 问候用户，并指出其名字 """
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username  = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when come back, " + username + "!")


greet_user()

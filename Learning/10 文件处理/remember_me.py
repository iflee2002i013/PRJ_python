from pathlib import Path
import json


def get_stored_userdata(path):
    """如果存储了用户信息，则返回用户信息，否则返回None"""
    if path.exists():
        contents = path.read_text()
        userdata = json.loads(contents)
        return userdata
    else:
        return None

def get_new_userdata(path):
    username = input("Please enter your username: ")
    age = input("Please enter your age: ")
    # 使用字典存储用户信息
    userdata = {"username": username, "age": age}

    contents = json.dumps(userdata)
    path.write_text(contents)

    return userdata

def greet_user():
    path = Path('userdata.json')
    userdata = get_stored_userdata(path)
    if userdata:
        """询问是否是该用户"""
        username = userdata['username']
        age = userdata['age']
        name_answer = input(f"Are you {username} (y/n)?")
        age_answer = input(f"You are {age} years old. (y/n)")
        if name_answer.lower() == 'y' and age_answer.lower() == 'y':
            print(f"Welcome back {username}!")
            return
        else:
            new_userdata = get_new_userdata(path)
            print(f"We will remember you as {new_userdata['username']},{new_userdata['age']}!")
            return
    else:
        new_userdata = get_new_userdata(path)
        print(f"We will remember you as {new_userdata['username']},{new_userdata['age']}!")

greet_user()


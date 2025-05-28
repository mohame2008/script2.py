import requests
from rich import print

def update_script():
    url='https://raw.githubusercontent.com/mohame2008/script2.py/387180260a1af50e3a470c7656963885763596b1/script2.py'
    may_name="fackyou"

    response= requests.get(url)
    if response.status_code==200: 

        with open(__file__,"wb") as f:
            f.write(response.content)

        print("update to the new version")
    else:
        print("no updates found")    
print("-----------------------")
print("-----------------------")
print("-----------------------")
update_script()
print("-----------------------")
print("[yellow]welcom [/]")
print("-----------------------")
name=input("enter ur name : ")
print("your name is : ",name)
print("-----------------------")

print("-----------------------")

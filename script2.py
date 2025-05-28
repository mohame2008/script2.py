import requests
from rich import print

def update_script():
    url='https://github.com/mohame2008/script2.py'
    response= requests.get(url)
    if response.status_code==200: 
        print("update to the new version")
    else:
        print("no updates found")    



update_script()
print("-----------------------")
print("[yellow]welcom [/]")
print("-----------------------")
name=input("enter ur name : ")
print("your name is : ",name)

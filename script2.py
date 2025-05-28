import requests
from rich import print

def update_script():
    url='https://raw.githubusercontent.com/mohame2008/script2.py/341457a525c5e5e0d9147e77c30574d2b01306da/script2.py'
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

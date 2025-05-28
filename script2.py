import requests
from rich import print

def update_script():
    url='file:///home/mohamed/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/script2.py'
    response= requests.get(url)
    if response.status_code==200: 

        with open(__file__,"wb") as f:
            f.write(response.content)

        print("update to the new version")
    else:
        print("no updates found")    


print("-----------------------")
update_script()
print("-----------------------")
print("[yellow]welcom [/]")
print("-----------------------")
name=input("enter ur name : ")
print("your name is : ",name)

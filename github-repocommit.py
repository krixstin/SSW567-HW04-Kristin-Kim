import requests
import json


username = "krixstin"
url1=f"https://api.github.com/users/{username}/repos"

repo = requests.get(url1).json() #list
repoNum=len(repo)

i=0
while i<repoNum:

    # Find name of the repository
    repoName = ""
    repoName=repo[i]['name']

    # Number of commit for repoName
    url2 = f"https://api.github.com/repos/{username}/{repoName}/commits"
    commits = len(requests.get(url2).json())

    print("Repo: ",repo[i]['name'],"Number of commits: ",commits)

    i+=1
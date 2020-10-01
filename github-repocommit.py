import requests
import json
import unittest

username = "krixstin"
url1=f"https://api.github.com/users/{username}/repos"

repo = requests.get(url1).json() #list
repoNum=len(repo)

k=0
while k<repoNum:

    # Find name of the repository
    repoName = ""
    repoName=repo[k]['name']

    # Number of commit for repoName
    url2 = f"https://api.github.com/repos/{username}/{repoName}/commits"
    commits = len(requests.get(url2).json())

    print("Repo: ",repo[i]['name'],"Number of commits: ",commits)
    k+=1
i=0


class MC(i,str(username),str(repoName)):
    pass

class RepoCommit(i,username,repoName):
    __metaclass__ = MC

    i=0
    # Find name of the repository
    repoName = ""
    repoName=repo[i]['name']

    # Number of commit for repoName
    url2 = f"https://api.github.com/repos/{username}/{repoName}/commits"
    commits = len(requests.get(url2).json())
    cl="Repo: "+repo[i]['name']+"Number of commits: "+str(commits)
    # return cl

class TestRepoCommit(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def RepoCommit(self):
        self.assertEqual(RepoCommit(0,s,s),'Repo:  githit Number of commits:  1', "first repo/commit chekced")
    def RepoCommit(self):
        self.assertEqual(RepoCommit(1),'Repo:  helloworld Number of commits:  2', "second repo/commit chekced")
    def RepoCommit(self):
        self.assertEqual(RepoCommit(2),'Repo:  kushal1223 Number of commits:  11', "third repo/commit chekced")
    def RepoCommit(self):
        self.assertEqual(RepoCommit(3),'Repo:  Runge-Kutta-Fehlberg Number of commits:  1', "forth repo/commit chekced")
    def RepoCommit(self):
        self.assertEqual(RepoCommit(4),'Repo:  SSW567-HW02-Kristin-Kim Number of commits:  6', "fifth repo/commit chekced")
    def RepoCommit(self):
        self.assertEqual(RepoCommit(5),'Repo:  SSW567-HW04-Kristin-Kim Number of commits:  8', "sixth repo/commit chekced")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


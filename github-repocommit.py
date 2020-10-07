import requests
import json
import unittest

username = "krixstin"
url1=f"https://api.github.com/users/{username}/repos"

repo = requests.get(url1).json() #list
repoNum=len(repo)


def RepoCommit(p):

    k = 0
    list = []
    i = 0
    p = 0

    while k<repoNum:

        # Find name of the repository
        repoName = ""
        repoName=repo[k]['name']

        # Number of commit for repoName
        url2 = f"https://api.github.com/repos/{username}/{repoName}/commits"
        commits = len(requests.get(url2).json())

        a=str("Repo: "+repo[i]['name']+" Number of commits: "+str(commits))
        list.append(a)

        k+=1
        i+=1
    # print("0st",list[0])
    # print("1st", list[1])
    # print("2st", list[2])
    # print("3st", list[3])
    # print("4st", list[4])
    # print("5st", list[5])
    return list[p]

# print (RepoCommit(1))
# print (RepoCommit(2))
# print (RepoCommit(3))
# print (RepoCommit(4))

class Test_Repo_Commit(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def RepoCommit(self):
        self.assertEqual(RepoCommit(0),'Repo:  githit Number of commits:  1', "first repo/commit chekced")
        self.assertEqual(RepoCommit(1),'Repo:  helloworld Number of commits:  2', "second repo/commit chekced")
        self.assertEqual(RepoCommit(2),'Repo:  kushal1223 Number of commits:  11', "third repo/commit chekced")
        self.assertEqual(RepoCommit(3),'Repo:  Runge-Kutta-Fehlberg Number of commits:  1', "forth repo/commit chekced")
        self.assertEqual(RepoCommit(4),'Repo:  SSW567-HW02-Kristin-Kim Number of commits:  6', "fifth repo/commit chekced")
        self.assertEqual(RepoCommit(5),'Repo:  SSW567-HW04-Kristin-Kim Number of commits:  8', "sixth repo/commit chekced")

if __name__ == '__main__':
    unittest.main()
import unittest

from GitHubAPI import git_hub_api

from typing import List,Any

class TestGitHubAPI(unittest.TestCase):
    def testgithubapi(self):
        """ Testing GitHubAPI"""
        lis: List[str] = git_hub_api("richkempinski")
        self.assertEqual(lis[0],'Repo: csp Number of commits: 2')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()



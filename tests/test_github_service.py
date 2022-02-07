import unittest
from unittest.mock import patch

from services.github import GitHubService

class TestGithubService(unittest.TestCase):
    def setUp(self):
        self.github_mock = {

        }
    
    def test_get_trending_repos(self):

        r = GitHubService.get_trending_repos()

        print(r)

        self.assertTrue(1==2)

    

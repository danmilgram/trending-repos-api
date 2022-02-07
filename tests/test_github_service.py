import unittest
from unittest.mock import patch
from services.github import GitHubService

class TestGithubService(unittest.TestCase):

    def setUp(self):
        self.mock_trending_repos = {
            "total_count": 2,
            "incomplete_results": False,
            "items": [{
                "id": 1,
                "language": "JavaScript",
                "html_url": "https://github.com/testuser/testrepo",
                "description":"Test Javascript Repo"
                },
                {
                "id": 2,
                "language": "Python",
                "html_url": "https://github.com/testuser2/testrepo2",
                "description":"Test Python Repo"
                },
                {
                "id": 3,
                "language": None,
                "html_url": "https://github.com/testuser3/testrepo3",
                "description":"Test Undefined language Repo"
                },                
            ]
        }
        
        self.mock_trending_repos_empty_response = {
            "total_count": 0,
            "incomplete_results": False,
            "items": []
        }
    @patch("services.github.GitHubService._fetch_trending_repos")
    def test_get_trending_repos_ok(self, fetch_mock):

        fetch_mock.return_value = self.mock_trending_repos

        date = "2020-01-01"

        r = GitHubService.get_trending_repos(date)

        expected_response = {
            'JavaScript': {
                'count': 1, 
                'repos': [
                    {
                        'url': 'https://github.com/testuser/testrepo', 
                        'description': 'Test Javascript Repo'
                    }
                ]
            }, 
            'Python': {
                'count': 1, 
                'repos': [
                    {
                        'url': 'https://github.com/testuser2/testrepo2', 
                        'description': 'Test Python Repo'
                    }
                ]
            }, 
            'undefined': {
                'count': 1, 
                'repos': [
                    {
                        'url': 'https://github.com/testuser3/testrepo3', 
                        'description': 'Test Undefined language Repo'
                    }
                ]
            }
        }

        self.assertTrue(r==expected_response)
        fetch_mock.assert_called_once()

    @patch("services.github.GitHubService._fetch_trending_repos")
    def test_get_trending_repos_empty_response(self, fetch_mock):

        fetch_mock.return_value = self.mock_trending_repos_empty_response

        date = "2020-01-01"

        r = GitHubService.get_trending_repos(date)

        self.assertTrue(r=={})

    

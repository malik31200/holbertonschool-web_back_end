#!/usr/bin/env python3
"""
Unit tests for client.py
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Test for GithubOrgClient
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Test for GithubOrgClient.org
        check that get_json is mocked
        and not actually executed
        """

        mock_get_json.return_value = {"login": org_name}

        client = GithubOrgClient(org_name)

        result = client.org

        self.assertEqual(result, {"login": org_name})

        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
            )

    def test_public_repos_url(self):
        """
        Test for GithubOrgClient._public_repos_url
        """
        payload = {
            "repos_url":  "https://api.github.com/orgs/google/repos"
        }

        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock
        ) as mock_org:

            mock_org.return_value = payload

            client = GithubOrgClient("google")

            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/google/repos"
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """ Test for GithubOrgClient.public_repos """
        payload = [
            {
                "name": "repo1"
            },
            {
                "name": "repo2"
            },
            {
                "name": "repo3"
            }
        ]

        mock_get_json.return_value = payload

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_url:

            mock_url.return_value = "https://api.github.com/orgs/google/repos"

            client = GithubOrgClient("ggogle")

            result = client.public_repos()

            self.assertEqual(
                result,
                ["repo1", "repo2", "repo3"]
            )

            mock_url.assert_called_once()

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google/repos"
            )

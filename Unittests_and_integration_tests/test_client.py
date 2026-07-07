#!/usr/bin/env python3
"""
Unit tests for client.py
"""

import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
from fixtures import (
    org_payload,
    repos_payload,
    expected_repos,
    apache2_repos,
)


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

            client = GithubOrgClient("google")

            result = client.public_repos()

            self.assertEqual(
                result,
                ["repo1", "repo2", "repo3"]
            )

            mock_url.assert_called_once()

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google/repos"
            )

    @parameterized.expand([
        (
            {"license": {"key": "my_license"}},
            "my_license",
            True
        ),
        (
            {"license": {"key": "other_license"}},
            "my_license",
            False
        ),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test for GithubOrgClient.has_license
        Check that has_license returns the expected value.
        """
        result = GithubOrgClient.has_license(repo, license_key)

        self.assertEqual(result, expected)


@parameterized_class(("org_payload", "repos_payload", "expected_repos", "apache2_repos"), [
    (
        org_payload,
        repos_payload,
        expected_repos,
        apache2_repos,
    )
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Test for GithubOrgClient.public_repos
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up the mock for requests.get.

        We only mock external HTTP requests.
        The rest of GithubOrgClient works normally.
        """

        # Create a patcher for requests.get
        cls.get_patcher = patch("requests.get")

        # Start the patch and save the mock object
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """
            Return different fake responses depending on the URL.
            """

            # Create a fake response object
            response = Mock()

            # If GithubOrgClient asks for organization information
            if url == GithubOrgClient.ORG_URL.format(org="google"):
                response.json.return_value = cls.org_payload

            # If GithubOrgClient asks for repositories
            elif url == cls.org_payload["repos_url"]:
                response.json.return_value = cls.repos_payload

            return response

        # Make requests.get use our side_effect function
        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Stop the requests.get patch after tests.
        """

        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test that public_repos returns expected repositories.
        """

        # Create a GithubOrgClient instance
        client = GithubOrgClient("google")

        # Call public_repos()
        result = client.public_repos()

        # Check that the repositories names are correct
        self.assertEqual(
            result,
            self.expected_repos
        )

    def test_public_repos_with_license(self):
        """
        Test that public_repos filters repositories by license.
        """

        client = GithubOrgClient("google")

        result = client.public_repos("apache-2.0")

        self.assertEqual(
            result,
            self.apache2_repos
        )

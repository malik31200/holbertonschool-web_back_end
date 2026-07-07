#!/usr/bin/env python3
"""
Unit tests for client.py
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


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

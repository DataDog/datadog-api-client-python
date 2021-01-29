# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi  # noqa: E501


class TestSecurityMonitoringApi(unittest.TestCase):
    """SecurityMonitoringApi unit test stubs"""

    def setUp(self):
        self.api = SecurityMonitoringApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_security_monitoring_rule(self):
        """Test case for create_security_monitoring_rule

        Create a detection rule  # noqa: E501
        """
        pass

    def test_delete_security_monitoring_rule(self):
        """Test case for delete_security_monitoring_rule

        Delete an existing rule  # noqa: E501
        """
        pass

    def test_get_security_monitoring_rule(self):
        """Test case for get_security_monitoring_rule

        Get a rule's details  # noqa: E501
        """
        pass

    def test_list_security_monitoring_rules(self):
        """Test case for list_security_monitoring_rules

        List rules  # noqa: E501
        """
        pass

    def test_update_security_monitoring_rule(self):
        """Test case for update_security_monitoring_rule

        Update an existing rule  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

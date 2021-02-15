# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.pager_duty_integration_api import PagerDutyIntegrationApi  # noqa: E501


class TestPagerDutyIntegrationApi(unittest.TestCase):
    """PagerDutyIntegrationApi unit test stubs"""

    def setUp(self):
        self.api = PagerDutyIntegrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_pager_duty_integration_service(self):
        """Test case for create_pager_duty_integration_service

        Create a new service object  # noqa: E501
        """
        pass

    def test_delete_pager_duty_integration_service(self):
        """Test case for delete_pager_duty_integration_service

        Delete a single service object  # noqa: E501
        """
        pass

    def test_get_pager_duty_integration_service(self):
        """Test case for get_pager_duty_integration_service

        Get a single service object  # noqa: E501
        """
        pass

    def test_update_pager_duty_integration_service(self):
        """Test case for update_pager_duty_integration_service

        Update a single service object  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

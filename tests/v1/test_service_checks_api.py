# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.service_checks_api import ServiceChecksApi  # noqa: E501


class TestServiceChecksApi(unittest.TestCase):
    """ServiceChecksApi unit test stubs"""

    def setUp(self):
        self.api = ServiceChecksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_submit_service_check(self):
        """Test case for submit_service_check

        Submit a Service Check  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

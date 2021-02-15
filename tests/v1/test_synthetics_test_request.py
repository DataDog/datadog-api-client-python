# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.http_method import HTTPMethod
from datadog_api_client.v1.model.synthetics_basic_auth import SyntheticsBasicAuth
from datadog_api_client.v1.model.synthetics_test_headers import SyntheticsTestHeaders
from datadog_api_client.v1.model.synthetics_test_request_certificate import SyntheticsTestRequestCertificate

globals()["HTTPMethod"] = HTTPMethod
globals()["SyntheticsBasicAuth"] = SyntheticsBasicAuth
globals()["SyntheticsTestHeaders"] = SyntheticsTestHeaders
globals()["SyntheticsTestRequestCertificate"] = SyntheticsTestRequestCertificate
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest


class TestSyntheticsTestRequest(unittest.TestCase):
    """SyntheticsTestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsTestRequest(self):
        """Test SyntheticsTestRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsTestRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

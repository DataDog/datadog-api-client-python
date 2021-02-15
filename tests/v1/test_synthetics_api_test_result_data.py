# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_error_code import SyntheticsErrorCode
from datadog_api_client.v1.model.synthetics_ssl_certificate import SyntheticsSSLCertificate
from datadog_api_client.v1.model.synthetics_test_process_status import SyntheticsTestProcessStatus
from datadog_api_client.v1.model.synthetics_timing import SyntheticsTiming

globals()["SyntheticsErrorCode"] = SyntheticsErrorCode
globals()["SyntheticsSSLCertificate"] = SyntheticsSSLCertificate
globals()["SyntheticsTestProcessStatus"] = SyntheticsTestProcessStatus
globals()["SyntheticsTiming"] = SyntheticsTiming
from datadog_api_client.v1.model.synthetics_api_test_result_data import SyntheticsAPITestResultData


class TestSyntheticsAPITestResultData(unittest.TestCase):
    """SyntheticsAPITestResultData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsAPITestResultData(self):
        """Test SyntheticsAPITestResultData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsAPITestResultData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

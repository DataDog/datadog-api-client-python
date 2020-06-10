# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import synthetics_error_code
except ImportError:
    synthetics_error_code = sys.modules[
        'datadog_api_client.v1.model.synthetics_error_code']
try:
    from datadog_api_client.v1.model import synthetics_ssl_certificate
except ImportError:
    synthetics_ssl_certificate = sys.modules[
        'datadog_api_client.v1.model.synthetics_ssl_certificate']
try:
    from datadog_api_client.v1.model import synthetics_test_process_status
except ImportError:
    synthetics_test_process_status = sys.modules[
        'datadog_api_client.v1.model.synthetics_test_process_status']
try:
    from datadog_api_client.v1.model import synthetics_timing
except ImportError:
    synthetics_timing = sys.modules[
        'datadog_api_client.v1.model.synthetics_timing']
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


if __name__ == '__main__':
    unittest.main()

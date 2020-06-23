# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import aws_logs_async_response_errors
except ImportError:
    aws_logs_async_response_errors = sys.modules[
        'datadog_api_client.v1.model.aws_logs_async_response_errors']
from datadog_api_client.v1.model.aws_logs_async_response import AWSLogsAsyncResponse


class TestAWSLogsAsyncResponse(unittest.TestCase):
    """AWSLogsAsyncResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAWSLogsAsyncResponse(self):
        """Test AWSLogsAsyncResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AWSLogsAsyncResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

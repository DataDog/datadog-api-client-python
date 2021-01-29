# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import slo_history_response_data
except ImportError:
    slo_history_response_data = sys.modules["datadog_api_client.v1.model.slo_history_response_data"]
try:
    from datadog_api_client.v1.model import slo_history_response_error
except ImportError:
    slo_history_response_error = sys.modules["datadog_api_client.v1.model.slo_history_response_error"]
from datadog_api_client.v1.model.slo_history_response import SLOHistoryResponse


class TestSLOHistoryResponse(unittest.TestCase):
    """SLOHistoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOHistoryResponse(self):
        """Test SLOHistoryResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOHistoryResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import slo_error_timeframe
except ImportError:
    slo_error_timeframe = sys.modules["datadog_api_client.v1.model.slo_error_timeframe"]
from datadog_api_client.v1.model.slo_bulk_delete_response_errors import SLOBulkDeleteResponseErrors


class TestSLOBulkDeleteResponseErrors(unittest.TestCase):
    """SLOBulkDeleteResponseErrors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOBulkDeleteResponseErrors(self):
        """Test SLOBulkDeleteResponseErrors"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOBulkDeleteResponseErrors()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

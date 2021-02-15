# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_error_timeframe import SLOErrorTimeframe

globals()["SLOErrorTimeframe"] = SLOErrorTimeframe
from datadog_api_client.v1.model.slo_bulk_delete_error import SLOBulkDeleteError


class TestSLOBulkDeleteError(unittest.TestCase):
    """SLOBulkDeleteError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOBulkDeleteError(self):
        """Test SLOBulkDeleteError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOBulkDeleteError()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

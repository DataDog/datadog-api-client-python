# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe

globals()["SLOTimeframe"] = SLOTimeframe
from datadog_api_client.v1.model.slo_bulk_delete import SLOBulkDelete


class TestSLOBulkDelete(unittest.TestCase):
    """SLOBulkDelete unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOBulkDelete(self):
        """Test SLOBulkDelete"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOBulkDelete()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_bulk_delete_error import SLOBulkDeleteError
from datadog_api_client.v1.model.slo_bulk_delete_response_data import SLOBulkDeleteResponseData

globals()["SLOBulkDeleteError"] = SLOBulkDeleteError
globals()["SLOBulkDeleteResponseData"] = SLOBulkDeleteResponseData
from datadog_api_client.v1.model.slo_bulk_delete_response import SLOBulkDeleteResponse


class TestSLOBulkDeleteResponse(unittest.TestCase):
    """SLOBulkDeleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOBulkDeleteResponse(self):
        """Test SLOBulkDeleteResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOBulkDeleteResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

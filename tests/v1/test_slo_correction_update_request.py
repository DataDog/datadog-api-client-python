# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_correction_update_data import SLOCorrectionUpdateData

globals()["SLOCorrectionUpdateData"] = SLOCorrectionUpdateData
from datadog_api_client.v1.model.slo_correction_update_request import SLOCorrectionUpdateRequest


class TestSLOCorrectionUpdateRequest(unittest.TestCase):
    """SLOCorrectionUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOCorrectionUpdateRequest(self):
        """Test SLOCorrectionUpdateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOCorrectionUpdateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

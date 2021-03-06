# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_correction import SLOCorrection

globals()["SLOCorrection"] = SLOCorrection
from datadog_api_client.v1.model.slo_correction_list_response import SLOCorrectionListResponse


class TestSLOCorrectionListResponse(unittest.TestCase):
    """SLOCorrectionListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOCorrectionListResponse(self):
        """Test SLOCorrectionListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOCorrectionListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

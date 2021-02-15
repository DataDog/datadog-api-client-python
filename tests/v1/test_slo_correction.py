# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_correction_response_attributes import SLOCorrectionResponseAttributes
from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType

globals()["SLOCorrectionResponseAttributes"] = SLOCorrectionResponseAttributes
globals()["SLOCorrectionType"] = SLOCorrectionType
from datadog_api_client.v1.model.slo_correction import SLOCorrection


class TestSLOCorrection(unittest.TestCase):
    """SLOCorrection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOCorrection(self):
        """Test SLOCorrection"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOCorrection()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

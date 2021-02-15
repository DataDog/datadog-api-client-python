# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.creator import Creator
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory

globals()["Creator"] = Creator
globals()["SLOCorrectionCategory"] = SLOCorrectionCategory
from datadog_api_client.v1.model.slo_correction_response_attributes import SLOCorrectionResponseAttributes


class TestSLOCorrectionResponseAttributes(unittest.TestCase):
    """SLOCorrectionResponseAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOCorrectionResponseAttributes(self):
        """Test SLOCorrectionResponseAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOCorrectionResponseAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

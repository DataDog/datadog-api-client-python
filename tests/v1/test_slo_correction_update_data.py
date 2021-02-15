# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType
from datadog_api_client.v1.model.slo_correction_update_request_attributes import SLOCorrectionUpdateRequestAttributes

globals()["SLOCorrectionType"] = SLOCorrectionType
globals()["SLOCorrectionUpdateRequestAttributes"] = SLOCorrectionUpdateRequestAttributes
from datadog_api_client.v1.model.slo_correction_update_data import SLOCorrectionUpdateData


class TestSLOCorrectionUpdateData(unittest.TestCase):
    """SLOCorrectionUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOCorrectionUpdateData(self):
        """Test SLOCorrectionUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOCorrectionUpdateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

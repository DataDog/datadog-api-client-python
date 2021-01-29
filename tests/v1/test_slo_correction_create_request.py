# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_correction_create_request_data import SLOCorrectionCreateRequestData

globals()["SLOCorrectionCreateRequestData"] = SLOCorrectionCreateRequestData
from datadog_api_client.v1.model.slo_correction_create_request import SLOCorrectionCreateRequest


class TestSLOCorrectionCreateRequest(unittest.TestCase):
    """SLOCorrectionCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOCorrectionCreateRequest(self):
        """Test SLOCorrectionCreateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOCorrectionCreateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

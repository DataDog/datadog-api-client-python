# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
globals()['SLOCorrectionCategory'] = SLOCorrectionCategory
from datadog_api_client.v1.model.slo_correction_update_request_attributes import SLOCorrectionUpdateRequestAttributes


class TestSLOCorrectionUpdateRequestAttributes(unittest.TestCase):
    """SLOCorrectionUpdateRequestAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOCorrectionUpdateRequestAttributes(self):
        """Test SLOCorrectionUpdateRequestAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOCorrectionUpdateRequestAttributes()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

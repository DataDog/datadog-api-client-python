# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.service_level_objective import ServiceLevelObjective

globals()["ServiceLevelObjective"] = ServiceLevelObjective
from datadog_api_client.v1.model.slo_list_response import SLOListResponse


class TestSLOListResponse(unittest.TestCase):
    """SLOListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOListResponse(self):
        """Test SLOListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

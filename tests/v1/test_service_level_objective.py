# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.creator import Creator
from datadog_api_client.v1.model.service_level_objective_query import ServiceLevelObjectiveQuery
from datadog_api_client.v1.model.slo_threshold import SLOThreshold
from datadog_api_client.v1.model.slo_type import SLOType

globals()["Creator"] = Creator
globals()["SLOThreshold"] = SLOThreshold
globals()["SLOType"] = SLOType
globals()["ServiceLevelObjectiveQuery"] = ServiceLevelObjectiveQuery
from datadog_api_client.v1.model.service_level_objective import ServiceLevelObjective


class TestServiceLevelObjective(unittest.TestCase):
    """ServiceLevelObjective unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceLevelObjective(self):
        """Test ServiceLevelObjective"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceLevelObjective()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

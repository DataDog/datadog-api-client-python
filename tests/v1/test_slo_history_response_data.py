# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_history_metrics import SLOHistoryMetrics
from datadog_api_client.v1.model.slo_history_sli_data import SLOHistorySLIData
from datadog_api_client.v1.model.slo_threshold import SLOThreshold
from datadog_api_client.v1.model.slo_type import SLOType
from datadog_api_client.v1.model.slo_type_numeric import SLOTypeNumeric

globals()["SLOHistoryMetrics"] = SLOHistoryMetrics
globals()["SLOHistorySLIData"] = SLOHistorySLIData
globals()["SLOThreshold"] = SLOThreshold
globals()["SLOType"] = SLOType
globals()["SLOTypeNumeric"] = SLOTypeNumeric
from datadog_api_client.v1.model.slo_history_response_data import SLOHistoryResponseData


class TestSLOHistoryResponseData(unittest.TestCase):
    """SLOHistoryResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOHistoryResponseData(self):
        """Test SLOHistoryResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOHistoryResponseData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

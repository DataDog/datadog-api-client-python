# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_monitoring_signal import SecurityMonitoringSignal
from datadog_api_client.v2.model.security_monitoring_signals_list_response_links import (
    SecurityMonitoringSignalsListResponseLinks,
)
from datadog_api_client.v2.model.security_monitoring_signals_list_response_meta import (
    SecurityMonitoringSignalsListResponseMeta,
)

globals()["SecurityMonitoringSignal"] = SecurityMonitoringSignal
globals()["SecurityMonitoringSignalsListResponseLinks"] = SecurityMonitoringSignalsListResponseLinks
globals()["SecurityMonitoringSignalsListResponseMeta"] = SecurityMonitoringSignalsListResponseMeta
from datadog_api_client.v2.model.security_monitoring_signals_list_response import SecurityMonitoringSignalsListResponse


class TestSecurityMonitoringSignalsListResponse(unittest.TestCase):
    """SecurityMonitoringSignalsListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityMonitoringSignalsListResponse(self):
        """Test SecurityMonitoringSignalsListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityMonitoringSignalsListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

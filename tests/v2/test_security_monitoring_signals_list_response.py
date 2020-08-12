# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import security_monitoring_signal
except ImportError:
    security_monitoring_signal = sys.modules[
        'datadog_api_client.v2.model.security_monitoring_signal']
try:
    from datadog_api_client.v2.model import security_monitoring_signals_list_response_links
except ImportError:
    security_monitoring_signals_list_response_links = sys.modules[
        'datadog_api_client.v2.model.security_monitoring_signals_list_response_links']
try:
    from datadog_api_client.v2.model import security_monitoring_signals_list_response_meta
except ImportError:
    security_monitoring_signals_list_response_meta = sys.modules[
        'datadog_api_client.v2.model.security_monitoring_signals_list_response_meta']
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


if __name__ == '__main__':
    unittest.main()

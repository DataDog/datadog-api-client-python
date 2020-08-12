# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import security_monitoring_signal_attributes
except ImportError:
    security_monitoring_signal_attributes = sys.modules[
        'datadog_api_client.v2.model.security_monitoring_signal_attributes']
try:
    from datadog_api_client.v2.model import security_monitoring_signal_type
except ImportError:
    security_monitoring_signal_type = sys.modules[
        'datadog_api_client.v2.model.security_monitoring_signal_type']
from datadog_api_client.v2.model.security_monitoring_signal import SecurityMonitoringSignal


class TestSecurityMonitoringSignal(unittest.TestCase):
    """SecurityMonitoringSignal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityMonitoringSignal(self):
        """Test SecurityMonitoringSignal"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityMonitoringSignal()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

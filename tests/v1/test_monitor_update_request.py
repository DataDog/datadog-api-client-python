# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import creator
except ImportError:
    creator = sys.modules[
        'datadog_api_client.v1.model.creator']
try:
    from datadog_api_client.v1.model import monitor_options
except ImportError:
    monitor_options = sys.modules[
        'datadog_api_client.v1.model.monitor_options']
try:
    from datadog_api_client.v1.model import monitor_overall_states
except ImportError:
    monitor_overall_states = sys.modules[
        'datadog_api_client.v1.model.monitor_overall_states']
try:
    from datadog_api_client.v1.model import monitor_state
except ImportError:
    monitor_state = sys.modules[
        'datadog_api_client.v1.model.monitor_state']
try:
    from datadog_api_client.v1.model import monitor_type
except ImportError:
    monitor_type = sys.modules[
        'datadog_api_client.v1.model.monitor_type']
from datadog_api_client.v1.model.monitor_update_request import MonitorUpdateRequest


class TestMonitorUpdateRequest(unittest.TestCase):
    """MonitorUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitorUpdateRequest(self):
        """Test MonitorUpdateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitorUpdateRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

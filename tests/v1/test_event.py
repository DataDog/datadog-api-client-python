# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import event_alert_type
except ImportError:
    event_alert_type = sys.modules[
        'datadog_api_client.v1.model.event_alert_type']
try:
    from datadog_api_client.v1.model import event_priority
except ImportError:
    event_priority = sys.modules[
        'datadog_api_client.v1.model.event_priority']
from datadog_api_client.v1.model.event import Event


class TestEvent(unittest.TestCase):
    """Event unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEvent(self):
        """Test Event"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Event()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

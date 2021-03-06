# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.event_alert_type import EventAlertType
from datadog_api_client.v1.model.event_priority import EventPriority

globals()["EventAlertType"] = EventAlertType
globals()["EventPriority"] = EventPriority
from datadog_api_client.v1.model.event_create_request import EventCreateRequest


class TestEventCreateRequest(unittest.TestCase):
    """EventCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventCreateRequest(self):
        """Test EventCreateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EventCreateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

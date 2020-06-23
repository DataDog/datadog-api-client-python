# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.events_api import EventsApi  # noqa: E501


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_event(self):
        """Test case for get_event

        Get an event  # noqa: E501
        """
        pass

    def test_list_events(self):
        """Test case for list_events

        Query the event stream  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

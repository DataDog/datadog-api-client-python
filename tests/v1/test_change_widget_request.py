# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import event_query_definition
except ImportError:
    event_query_definition = sys.modules["datadog_api_client.v1.model.event_query_definition"]
try:
    from datadog_api_client.v1.model import log_query_definition
except ImportError:
    log_query_definition = sys.modules["datadog_api_client.v1.model.log_query_definition"]
try:
    from datadog_api_client.v1.model import process_query_definition
except ImportError:
    process_query_definition = sys.modules["datadog_api_client.v1.model.process_query_definition"]
try:
    from datadog_api_client.v1.model import widget_change_type
except ImportError:
    widget_change_type = sys.modules["datadog_api_client.v1.model.widget_change_type"]
try:
    from datadog_api_client.v1.model import widget_compare_to
except ImportError:
    widget_compare_to = sys.modules["datadog_api_client.v1.model.widget_compare_to"]
try:
    from datadog_api_client.v1.model import widget_order_by
except ImportError:
    widget_order_by = sys.modules["datadog_api_client.v1.model.widget_order_by"]
try:
    from datadog_api_client.v1.model import widget_sort
except ImportError:
    widget_sort = sys.modules["datadog_api_client.v1.model.widget_sort"]
from datadog_api_client.v1.model.change_widget_request import ChangeWidgetRequest


class TestChangeWidgetRequest(unittest.TestCase):
    """ChangeWidgetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChangeWidgetRequest(self):
        """Test ChangeWidgetRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChangeWidgetRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

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
    from datadog_api_client.v1.model import timeseries_widget_request_metadata
except ImportError:
    timeseries_widget_request_metadata = sys.modules["datadog_api_client.v1.model.timeseries_widget_request_metadata"]
try:
    from datadog_api_client.v1.model import widget_display_type
except ImportError:
    widget_display_type = sys.modules["datadog_api_client.v1.model.widget_display_type"]
try:
    from datadog_api_client.v1.model import widget_request_style
except ImportError:
    widget_request_style = sys.modules["datadog_api_client.v1.model.widget_request_style"]
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest


class TestTimeseriesWidgetRequest(unittest.TestCase):
    """TimeseriesWidgetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeseriesWidgetRequest(self):
        """Test TimeseriesWidgetRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimeseriesWidgetRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

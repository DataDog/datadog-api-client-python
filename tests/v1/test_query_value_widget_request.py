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
    event_query_definition = sys.modules[
        'datadog_api_client.v1.model.event_query_definition']
try:
    from datadog_api_client.v1.model import log_query_definition
except ImportError:
    log_query_definition = sys.modules[
        'datadog_api_client.v1.model.log_query_definition']
try:
    from datadog_api_client.v1.model import process_query_definition
except ImportError:
    process_query_definition = sys.modules[
        'datadog_api_client.v1.model.process_query_definition']
try:
    from datadog_api_client.v1.model import widget_aggregator
except ImportError:
    widget_aggregator = sys.modules[
        'datadog_api_client.v1.model.widget_aggregator']
try:
    from datadog_api_client.v1.model import widget_conditional_format
except ImportError:
    widget_conditional_format = sys.modules[
        'datadog_api_client.v1.model.widget_conditional_format']
from datadog_api_client.v1.model.query_value_widget_request import QueryValueWidgetRequest


class TestQueryValueWidgetRequest(unittest.TestCase):
    """QueryValueWidgetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQueryValueWidgetRequest(self):
        """Test QueryValueWidgetRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QueryValueWidgetRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

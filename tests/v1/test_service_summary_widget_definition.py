# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.service_summary_widget_definition_type import ServiceSummaryWidgetDefinitionType
from datadog_api_client.v1.model.widget_service_summary_display_format import WidgetServiceSummaryDisplayFormat
from datadog_api_client.v1.model.widget_size_format import WidgetSizeFormat
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

globals()["ServiceSummaryWidgetDefinitionType"] = ServiceSummaryWidgetDefinitionType
globals()["WidgetServiceSummaryDisplayFormat"] = WidgetServiceSummaryDisplayFormat
globals()["WidgetSizeFormat"] = WidgetSizeFormat
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
from datadog_api_client.v1.model.service_summary_widget_definition import ServiceSummaryWidgetDefinition


class TestServiceSummaryWidgetDefinition(unittest.TestCase):
    """ServiceSummaryWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceSummaryWidgetDefinition(self):
        """Test ServiceSummaryWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceSummaryWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

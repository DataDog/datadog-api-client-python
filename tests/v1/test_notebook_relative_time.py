# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.widget_live_span import WidgetLiveSpan

globals()["WidgetLiveSpan"] = WidgetLiveSpan
from datadog_api_client.v1.model.notebook_relative_time import NotebookRelativeTime


class TestNotebookRelativeTime(unittest.TestCase):
    """NotebookRelativeTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookRelativeTime(self):
        """Test NotebookRelativeTime"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookRelativeTime()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

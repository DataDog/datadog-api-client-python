# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_absolute_time import NotebookAbsoluteTime
from datadog_api_client.v1.model.notebook_relative_time import NotebookRelativeTime
from datadog_api_client.v1.model.widget_live_span import WidgetLiveSpan

globals()["NotebookAbsoluteTime"] = NotebookAbsoluteTime
globals()["NotebookRelativeTime"] = NotebookRelativeTime
globals()["WidgetLiveSpan"] = WidgetLiveSpan
from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime


class TestNotebookGlobalTime(unittest.TestCase):
    """NotebookGlobalTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookGlobalTime(self):
        """Test NotebookGlobalTime"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookGlobalTime()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

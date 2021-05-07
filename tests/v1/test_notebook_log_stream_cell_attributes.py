# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.log_stream_widget_definition import LogStreamWidgetDefinition
from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime
from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize

globals()["LogStreamWidgetDefinition"] = LogStreamWidgetDefinition
globals()["NotebookCellTime"] = NotebookCellTime
globals()["NotebookGraphSize"] = NotebookGraphSize
from datadog_api_client.v1.model.notebook_log_stream_cell_attributes import NotebookLogStreamCellAttributes


class TestNotebookLogStreamCellAttributes(unittest.TestCase):
    """NotebookLogStreamCellAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookLogStreamCellAttributes(self):
        """Test NotebookLogStreamCellAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookLogStreamCellAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

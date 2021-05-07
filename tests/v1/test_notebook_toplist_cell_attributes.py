# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime
from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
from datadog_api_client.v1.model.toplist_widget_definition import ToplistWidgetDefinition

globals()["NotebookCellTime"] = NotebookCellTime
globals()["NotebookGraphSize"] = NotebookGraphSize
globals()["NotebookSplitBy"] = NotebookSplitBy
globals()["ToplistWidgetDefinition"] = ToplistWidgetDefinition
from datadog_api_client.v1.model.notebook_toplist_cell_attributes import NotebookToplistCellAttributes


class TestNotebookToplistCellAttributes(unittest.TestCase):
    """NotebookToplistCellAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookToplistCellAttributes(self):
        """Test NotebookToplistCellAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookToplistCellAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

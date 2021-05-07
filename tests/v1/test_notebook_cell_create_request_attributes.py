# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.log_stream_widget_definition import LogStreamWidgetDefinition
from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime
from datadog_api_client.v1.model.notebook_distribution_cell_attributes import NotebookDistributionCellAttributes
from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
from datadog_api_client.v1.model.notebook_heat_map_cell_attributes import NotebookHeatMapCellAttributes
from datadog_api_client.v1.model.notebook_log_stream_cell_attributes import NotebookLogStreamCellAttributes
from datadog_api_client.v1.model.notebook_markdown_cell_attributes import NotebookMarkdownCellAttributes
from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
from datadog_api_client.v1.model.notebook_timeseries_cell_attributes import NotebookTimeseriesCellAttributes
from datadog_api_client.v1.model.notebook_toplist_cell_attributes import NotebookToplistCellAttributes

globals()["LogStreamWidgetDefinition"] = LogStreamWidgetDefinition
globals()["NotebookCellTime"] = NotebookCellTime
globals()["NotebookDistributionCellAttributes"] = NotebookDistributionCellAttributes
globals()["NotebookGraphSize"] = NotebookGraphSize
globals()["NotebookHeatMapCellAttributes"] = NotebookHeatMapCellAttributes
globals()["NotebookLogStreamCellAttributes"] = NotebookLogStreamCellAttributes
globals()["NotebookMarkdownCellAttributes"] = NotebookMarkdownCellAttributes
globals()["NotebookSplitBy"] = NotebookSplitBy
globals()["NotebookTimeseriesCellAttributes"] = NotebookTimeseriesCellAttributes
globals()["NotebookToplistCellAttributes"] = NotebookToplistCellAttributes
from datadog_api_client.v1.model.notebook_cell_create_request_attributes import NotebookCellCreateRequestAttributes


class TestNotebookCellCreateRequestAttributes(unittest.TestCase):
    """NotebookCellCreateRequestAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookCellCreateRequestAttributes(self):
        """Test NotebookCellCreateRequestAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookCellCreateRequestAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

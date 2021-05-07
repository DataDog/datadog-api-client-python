# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.distribution_widget_definition import DistributionWidgetDefinition
from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime
from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy

globals()["DistributionWidgetDefinition"] = DistributionWidgetDefinition
globals()["NotebookCellTime"] = NotebookCellTime
globals()["NotebookGraphSize"] = NotebookGraphSize
globals()["NotebookSplitBy"] = NotebookSplitBy
from datadog_api_client.v1.model.notebook_distribution_cell_attributes import NotebookDistributionCellAttributes


class TestNotebookDistributionCellAttributes(unittest.TestCase):
    """NotebookDistributionCellAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookDistributionCellAttributes(self):
        """Test NotebookDistributionCellAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookDistributionCellAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

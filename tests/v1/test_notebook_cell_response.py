# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType
from datadog_api_client.v1.model.notebook_cell_response_attributes import NotebookCellResponseAttributes

globals()["NotebookCellResourceType"] = NotebookCellResourceType
globals()["NotebookCellResponseAttributes"] = NotebookCellResponseAttributes
from datadog_api_client.v1.model.notebook_cell_response import NotebookCellResponse


class TestNotebookCellResponse(unittest.TestCase):
    """NotebookCellResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookCellResponse(self):
        """Test NotebookCellResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookCellResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest
from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType
from datadog_api_client.v1.model.notebook_cell_update_request import NotebookCellUpdateRequest
from datadog_api_client.v1.model.notebook_cell_update_request_attributes import NotebookCellUpdateRequestAttributes

globals()["NotebookCellCreateRequest"] = NotebookCellCreateRequest
globals()["NotebookCellResourceType"] = NotebookCellResourceType
globals()["NotebookCellUpdateRequest"] = NotebookCellUpdateRequest
globals()["NotebookCellUpdateRequestAttributes"] = NotebookCellUpdateRequestAttributes
from datadog_api_client.v1.model.notebook_update_cell import NotebookUpdateCell


class TestNotebookUpdateCell(unittest.TestCase):
    """NotebookUpdateCell unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookUpdateCell(self):
        """Test NotebookUpdateCell"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookUpdateCell()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_cell_create_request_attributes import NotebookCellCreateRequestAttributes
from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType

globals()["NotebookCellCreateRequestAttributes"] = NotebookCellCreateRequestAttributes
globals()["NotebookCellResourceType"] = NotebookCellResourceType
from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest


class TestNotebookCellCreateRequest(unittest.TestCase):
    """NotebookCellCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookCellCreateRequest(self):
        """Test NotebookCellCreateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookCellCreateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

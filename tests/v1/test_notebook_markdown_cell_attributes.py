# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_markdown_cell_definition import NotebookMarkdownCellDefinition

globals()["NotebookMarkdownCellDefinition"] = NotebookMarkdownCellDefinition
from datadog_api_client.v1.model.notebook_markdown_cell_attributes import NotebookMarkdownCellAttributes


class TestNotebookMarkdownCellAttributes(unittest.TestCase):
    """NotebookMarkdownCellAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookMarkdownCellAttributes(self):
        """Test NotebookMarkdownCellAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookMarkdownCellAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

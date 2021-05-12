# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_author import NotebookAuthor
from datadog_api_client.v1.model.notebook_cell_response import NotebookCellResponse
from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime
from datadog_api_client.v1.model.notebook_status import NotebookStatus

globals()["NotebookAuthor"] = NotebookAuthor
globals()["NotebookCellResponse"] = NotebookCellResponse
globals()["NotebookGlobalTime"] = NotebookGlobalTime
globals()["NotebookStatus"] = NotebookStatus
from datadog_api_client.v1.model.notebook_response_data_attributes import NotebookResponseDataAttributes


class TestNotebookResponseDataAttributes(unittest.TestCase):
    """NotebookResponseDataAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookResponseDataAttributes(self):
        """Test NotebookResponseDataAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookResponseDataAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

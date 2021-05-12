# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest
from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime
from datadog_api_client.v1.model.notebook_status import NotebookStatus

globals()["NotebookCellCreateRequest"] = NotebookCellCreateRequest
globals()["NotebookGlobalTime"] = NotebookGlobalTime
globals()["NotebookStatus"] = NotebookStatus
from datadog_api_client.v1.model.notebook_create_data_attributes import NotebookCreateDataAttributes


class TestNotebookCreateDataAttributes(unittest.TestCase):
    """NotebookCreateDataAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookCreateDataAttributes(self):
        """Test NotebookCreateDataAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookCreateDataAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

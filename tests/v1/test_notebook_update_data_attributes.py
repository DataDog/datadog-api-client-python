# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime
from datadog_api_client.v1.model.notebook_status import NotebookStatus
from datadog_api_client.v1.model.notebook_update_cell import NotebookUpdateCell

globals()["NotebookGlobalTime"] = NotebookGlobalTime
globals()["NotebookStatus"] = NotebookStatus
globals()["NotebookUpdateCell"] = NotebookUpdateCell
from datadog_api_client.v1.model.notebook_update_data_attributes import NotebookUpdateDataAttributes


class TestNotebookUpdateDataAttributes(unittest.TestCase):
    """NotebookUpdateDataAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookUpdateDataAttributes(self):
        """Test NotebookUpdateDataAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookUpdateDataAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

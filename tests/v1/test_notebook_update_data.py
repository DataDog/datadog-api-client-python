# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_resource_type import NotebookResourceType
from datadog_api_client.v1.model.notebook_update_data_attributes import NotebookUpdateDataAttributes

globals()["NotebookResourceType"] = NotebookResourceType
globals()["NotebookUpdateDataAttributes"] = NotebookUpdateDataAttributes
from datadog_api_client.v1.model.notebook_update_data import NotebookUpdateData


class TestNotebookUpdateData(unittest.TestCase):
    """NotebookUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookUpdateData(self):
        """Test NotebookUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookUpdateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_create_data import NotebookCreateData

globals()["NotebookCreateData"] = NotebookCreateData
from datadog_api_client.v1.model.notebook_create_request import NotebookCreateRequest


class TestNotebookCreateRequest(unittest.TestCase):
    """NotebookCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebookCreateRequest(self):
        """Test NotebookCreateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebookCreateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

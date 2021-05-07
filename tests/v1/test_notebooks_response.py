# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebook_response_data import NotebookResponseData
from datadog_api_client.v1.model.notebooks_response_meta import NotebooksResponseMeta

globals()["NotebookResponseData"] = NotebookResponseData
globals()["NotebooksResponseMeta"] = NotebooksResponseMeta
from datadog_api_client.v1.model.notebooks_response import NotebooksResponse


class TestNotebooksResponse(unittest.TestCase):
    """NotebooksResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebooksResponse(self):
        """Test NotebooksResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebooksResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

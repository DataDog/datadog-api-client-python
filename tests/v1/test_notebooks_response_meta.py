# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.notebooks_response_page import NotebooksResponsePage

globals()["NotebooksResponsePage"] = NotebooksResponsePage
from datadog_api_client.v1.model.notebooks_response_meta import NotebooksResponseMeta


class TestNotebooksResponseMeta(unittest.TestCase):
    """NotebooksResponseMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotebooksResponseMeta(self):
        """Test NotebooksResponseMeta"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotebooksResponseMeta()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

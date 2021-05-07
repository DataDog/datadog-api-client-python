# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.notebooks_api import NotebooksApi  # noqa: E501


class TestNotebooksApi(unittest.TestCase):
    """NotebooksApi unit test stubs"""

    def setUp(self):
        self.api = NotebooksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_notebook(self):
        """Test case for create_notebook

        Create a notebook  # noqa: E501
        """
        pass

    def test_delete_notebook(self):
        """Test case for delete_notebook

        Delete a notebook  # noqa: E501
        """
        pass

    def test_get_notebook(self):
        """Test case for get_notebook

        Get a notebook  # noqa: E501
        """
        pass

    def test_list_notebooks(self):
        """Test case for list_notebooks

        Get all notebooks  # noqa: E501
        """
        pass

    def test_update_notebook(self):
        """Test case for update_notebook

        Update a notebook  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

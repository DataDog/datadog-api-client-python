# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.tags_api import TagsApi  # noqa: E501


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self):
        self.api = TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_host_tags(self):
        """Test case for create_host_tags

        Add tags to a host  # noqa: E501
        """
        pass

    def test_delete_host_tags(self):
        """Test case for delete_host_tags

        Remove host tags  # noqa: E501
        """
        pass

    def test_get_host_tags(self):
        """Test case for get_host_tags

        Get host tags  # noqa: E501
        """
        pass

    def test_list_host_tags(self):
        """Test case for list_host_tags

        Get Tags  # noqa: E501
        """
        pass

    def test_update_host_tags(self):
        """Test case for update_host_tags

        Update host tags  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

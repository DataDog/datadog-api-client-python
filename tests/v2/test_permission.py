# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import permission_attributes
except ImportError:
    permission_attributes = sys.modules[
        'datadog_api_client.v2.model.permission_attributes']
try:
    from datadog_api_client.v2.model import permissions_type
except ImportError:
    permissions_type = sys.modules[
        'datadog_api_client.v2.model.permissions_type']
from datadog_api_client.v2.model.permission import Permission


class TestPermission(unittest.TestCase):
    """Permission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPermission(self):
        """Test Permission"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Permission()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

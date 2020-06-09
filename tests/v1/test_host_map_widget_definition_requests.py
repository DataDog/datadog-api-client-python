# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import host_map_request
except ImportError:
    host_map_request = sys.modules[
        'datadog_api_client.v1.model.host_map_request']
from datadog_api_client.v1.model.host_map_widget_definition_requests import HostMapWidgetDefinitionRequests


class TestHostMapWidgetDefinitionRequests(unittest.TestCase):
    """HostMapWidgetDefinitionRequests unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHostMapWidgetDefinitionRequests(self):
        """Test HostMapWidgetDefinitionRequests"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HostMapWidgetDefinitionRequests()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

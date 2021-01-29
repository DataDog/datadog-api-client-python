# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import host_meta
except ImportError:
    host_meta = sys.modules["datadog_api_client.v1.model.host_meta"]
try:
    from datadog_api_client.v1.model import host_metrics
except ImportError:
    host_metrics = sys.modules["datadog_api_client.v1.model.host_metrics"]
from datadog_api_client.v1.model.host import Host


class TestHost(unittest.TestCase):
    """Host unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHost(self):
        """Test Host"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Host()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

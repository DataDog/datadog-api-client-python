# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.host_meta import HostMeta
from datadog_api_client.v1.model.host_metrics import HostMetrics

globals()["HostMeta"] = HostMeta
globals()["HostMetrics"] = HostMetrics
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

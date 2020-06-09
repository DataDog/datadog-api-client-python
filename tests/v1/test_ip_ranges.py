# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import ip_prefixes_agents
except ImportError:
    ip_prefixes_agents = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_agents']
try:
    from datadog_api_client.v1.model import ip_prefixes_api
except ImportError:
    ip_prefixes_api = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_api']
try:
    from datadog_api_client.v1.model import ip_prefixes_apm
except ImportError:
    ip_prefixes_apm = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_apm']
try:
    from datadog_api_client.v1.model import ip_prefixes_logs
except ImportError:
    ip_prefixes_logs = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_logs']
try:
    from datadog_api_client.v1.model import ip_prefixes_process
except ImportError:
    ip_prefixes_process = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_process']
try:
    from datadog_api_client.v1.model import ip_prefixes_synthetics
except ImportError:
    ip_prefixes_synthetics = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_synthetics']
try:
    from datadog_api_client.v1.model import ip_prefixes_webhooks
except ImportError:
    ip_prefixes_webhooks = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_webhooks']
from datadog_api_client.v1.model.ip_ranges import IPRanges


class TestIPRanges(unittest.TestCase):
    """IPRanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIPRanges(self):
        """Test IPRanges"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IPRanges()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

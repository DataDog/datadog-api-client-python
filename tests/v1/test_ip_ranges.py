# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.ip_prefixes_agents import IPPrefixesAgents
from datadog_api_client.v1.model.ip_prefixes_api import IPPrefixesAPI
from datadog_api_client.v1.model.ip_prefixes_apm import IPPrefixesAPM
from datadog_api_client.v1.model.ip_prefixes_logs import IPPrefixesLogs
from datadog_api_client.v1.model.ip_prefixes_process import IPPrefixesProcess
from datadog_api_client.v1.model.ip_prefixes_synthetics import IPPrefixesSynthetics
from datadog_api_client.v1.model.ip_prefixes_webhooks import IPPrefixesWebhooks

globals()["IPPrefixesAPI"] = IPPrefixesAPI
globals()["IPPrefixesAPM"] = IPPrefixesAPM
globals()["IPPrefixesAgents"] = IPPrefixesAgents
globals()["IPPrefixesLogs"] = IPPrefixesLogs
globals()["IPPrefixesProcess"] = IPPrefixesProcess
globals()["IPPrefixesSynthetics"] = IPPrefixesSynthetics
globals()["IPPrefixesWebhooks"] = IPPrefixesWebhooks
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


if __name__ == "__main__":
    unittest.main()

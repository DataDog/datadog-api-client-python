# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import usage_timeseries_hour
except ImportError:
    usage_timeseries_hour = sys.modules[
        'datadog_api_client.v1.model.usage_timeseries_hour']
from datadog_api_client.v1.model.usage_timeseries_response import UsageTimeseriesResponse


class TestUsageTimeseriesResponse(unittest.TestCase):
    """UsageTimeseriesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageTimeseriesResponse(self):
        """Test UsageTimeseriesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageTimeseriesResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

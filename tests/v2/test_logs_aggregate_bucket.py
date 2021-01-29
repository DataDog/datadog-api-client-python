# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import logs_aggregate_bucket_value
except ImportError:
    logs_aggregate_bucket_value = sys.modules["datadog_api_client.v2.model.logs_aggregate_bucket_value"]
from datadog_api_client.v2.model.logs_aggregate_bucket import LogsAggregateBucket


class TestLogsAggregateBucket(unittest.TestCase):
    """LogsAggregateBucket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsAggregateBucket(self):
        """Test LogsAggregateBucket"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsAggregateBucket()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

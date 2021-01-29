# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_incident_management_hour import UsageIncidentManagementHour

globals()["UsageIncidentManagementHour"] = UsageIncidentManagementHour
from datadog_api_client.v1.model.usage_incident_management_response import UsageIncidentManagementResponse


class TestUsageIncidentManagementResponse(unittest.TestCase):
    """UsageIncidentManagementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageIncidentManagementResponse(self):
        """Test UsageIncidentManagementResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageIncidentManagementResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

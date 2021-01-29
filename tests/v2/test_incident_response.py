# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_response_data import IncidentResponseData
from datadog_api_client.v2.model.incident_response_included_item import IncidentResponseIncludedItem

globals()["IncidentResponseData"] = IncidentResponseData
globals()["IncidentResponseIncludedItem"] = IncidentResponseIncludedItem
from datadog_api_client.v2.model.incident_response import IncidentResponse


class TestIncidentResponse(unittest.TestCase):
    """IncidentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentResponse(self):
        """Test IncidentResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

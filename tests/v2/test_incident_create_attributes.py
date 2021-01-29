# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
from datadog_api_client.v2.model.incident_timeline_cell_create_attributes import IncidentTimelineCellCreateAttributes

globals()["IncidentFieldAttributes"] = IncidentFieldAttributes
globals()["IncidentTimelineCellCreateAttributes"] = IncidentTimelineCellCreateAttributes
from datadog_api_client.v2.model.incident_create_attributes import IncidentCreateAttributes


class TestIncidentCreateAttributes(unittest.TestCase):
    """IncidentCreateAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentCreateAttributes(self):
        """Test IncidentCreateAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentCreateAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

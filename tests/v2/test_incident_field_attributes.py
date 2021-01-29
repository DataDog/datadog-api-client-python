# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_field_attributes_multiple_value import IncidentFieldAttributesMultipleValue
from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
from datadog_api_client.v2.model.incident_field_attributes_value_type import IncidentFieldAttributesValueType

globals()["IncidentFieldAttributesMultipleValue"] = IncidentFieldAttributesMultipleValue
globals()["IncidentFieldAttributesSingleValue"] = IncidentFieldAttributesSingleValue
globals()["IncidentFieldAttributesValueType"] = IncidentFieldAttributesValueType
from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes


class TestIncidentFieldAttributes(unittest.TestCase):
    """IncidentFieldAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentFieldAttributes(self):
        """Test IncidentFieldAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentFieldAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

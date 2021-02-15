# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_response_data import IncidentResponseData
from datadog_api_client.v2.model.incident_response_included_item import IncidentResponseIncludedItem
from datadog_api_client.v2.model.incident_services_response_meta import IncidentServicesResponseMeta

globals()["IncidentResponseData"] = IncidentResponseData
globals()["IncidentResponseIncludedItem"] = IncidentResponseIncludedItem
globals()["IncidentServicesResponseMeta"] = IncidentServicesResponseMeta
from datadog_api_client.v2.model.incidents_response import IncidentsResponse


class TestIncidentsResponse(unittest.TestCase):
    """IncidentsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentsResponse(self):
        """Test IncidentsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

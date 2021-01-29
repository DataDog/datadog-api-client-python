# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.application_key_relationships import ApplicationKeyRelationships
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType
from datadog_api_client.v2.model.partial_application_key_attributes import PartialApplicationKeyAttributes

globals()["ApplicationKeyRelationships"] = ApplicationKeyRelationships
globals()["ApplicationKeysType"] = ApplicationKeysType
globals()["PartialApplicationKeyAttributes"] = PartialApplicationKeyAttributes
from datadog_api_client.v2.model.partial_application_key import PartialApplicationKey


class TestPartialApplicationKey(unittest.TestCase):
    """PartialApplicationKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPartialApplicationKey(self):
        """Test PartialApplicationKey"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PartialApplicationKey()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

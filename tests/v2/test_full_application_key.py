# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.application_key_relationships import ApplicationKeyRelationships
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType
from datadog_api_client.v2.model.full_application_key_attributes import FullApplicationKeyAttributes

globals()["ApplicationKeyRelationships"] = ApplicationKeyRelationships
globals()["ApplicationKeysType"] = ApplicationKeysType
globals()["FullApplicationKeyAttributes"] = FullApplicationKeyAttributes
from datadog_api_client.v2.model.full_application_key import FullApplicationKey


class TestFullApplicationKey(unittest.TestCase):
    """FullApplicationKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFullApplicationKey(self):
        """Test FullApplicationKey"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FullApplicationKey()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

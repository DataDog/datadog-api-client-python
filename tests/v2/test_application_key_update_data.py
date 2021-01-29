# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.application_key_update_attributes import ApplicationKeyUpdateAttributes
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

globals()["ApplicationKeyUpdateAttributes"] = ApplicationKeyUpdateAttributes
globals()["ApplicationKeysType"] = ApplicationKeysType
from datadog_api_client.v2.model.application_key_update_data import ApplicationKeyUpdateData


class TestApplicationKeyUpdateData(unittest.TestCase):
    """ApplicationKeyUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationKeyUpdateData(self):
        """Test ApplicationKeyUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationKeyUpdateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_private_location_secrets import SyntheticsPrivateLocationSecrets

globals()["SyntheticsPrivateLocationSecrets"] = SyntheticsPrivateLocationSecrets
from datadog_api_client.v1.model.synthetics_private_location import SyntheticsPrivateLocation


class TestSyntheticsPrivateLocation(unittest.TestCase):
    """SyntheticsPrivateLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsPrivateLocation(self):
        """Test SyntheticsPrivateLocation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsPrivateLocation()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

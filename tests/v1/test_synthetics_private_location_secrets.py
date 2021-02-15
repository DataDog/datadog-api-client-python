# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_private_location_secrets_authentication import (
    SyntheticsPrivateLocationSecretsAuthentication,
)
from datadog_api_client.v1.model.synthetics_private_location_secrets_config_decryption import (
    SyntheticsPrivateLocationSecretsConfigDecryption,
)

globals()["SyntheticsPrivateLocationSecretsAuthentication"] = SyntheticsPrivateLocationSecretsAuthentication
globals()["SyntheticsPrivateLocationSecretsConfigDecryption"] = SyntheticsPrivateLocationSecretsConfigDecryption
from datadog_api_client.v1.model.synthetics_private_location_secrets import SyntheticsPrivateLocationSecrets


class TestSyntheticsPrivateLocationSecrets(unittest.TestCase):
    """SyntheticsPrivateLocationSecrets unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsPrivateLocationSecrets(self):
        """Test SyntheticsPrivateLocationSecrets"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsPrivateLocationSecrets()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_browser_variable_type import SyntheticsBrowserVariableType

globals()["SyntheticsBrowserVariableType"] = SyntheticsBrowserVariableType
from datadog_api_client.v1.model.synthetics_browser_variable import SyntheticsBrowserVariable


class TestSyntheticsBrowserVariable(unittest.TestCase):
    """SyntheticsBrowserVariable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsBrowserVariable(self):
        """Test SyntheticsBrowserVariable"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsBrowserVariable()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

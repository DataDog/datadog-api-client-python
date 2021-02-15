# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_ci_test import SyntheticsCITest

globals()["SyntheticsCITest"] = SyntheticsCITest
from datadog_api_client.v1.model.synthetics_ci_test_body import SyntheticsCITestBody


class TestSyntheticsCITestBody(unittest.TestCase):
    """SyntheticsCITestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsCITestBody(self):
        """Test SyntheticsCITestBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsCITestBody()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

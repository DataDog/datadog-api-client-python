# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_api_step_subtype import SyntheticsAPIStepSubtype
from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion
from datadog_api_client.v1.model.synthetics_parsing_options import SyntheticsParsingOptions
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

globals()["SyntheticsAPIStepSubtype"] = SyntheticsAPIStepSubtype
globals()["SyntheticsAssertion"] = SyntheticsAssertion
globals()["SyntheticsParsingOptions"] = SyntheticsParsingOptions
globals()["SyntheticsTestRequest"] = SyntheticsTestRequest
from datadog_api_client.v1.model.synthetics_api_step import SyntheticsAPIStep


class TestSyntheticsAPIStep(unittest.TestCase):
    """SyntheticsAPIStep unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsAPIStep(self):
        """Test SyntheticsAPIStep"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsAPIStep()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

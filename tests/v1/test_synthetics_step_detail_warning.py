# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_warning_type import SyntheticsWarningType

globals()["SyntheticsWarningType"] = SyntheticsWarningType
from datadog_api_client.v1.model.synthetics_step_detail_warning import SyntheticsStepDetailWarning


class TestSyntheticsStepDetailWarning(unittest.TestCase):
    """SyntheticsStepDetailWarning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsStepDetailWarning(self):
        """Test SyntheticsStepDetailWarning"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsStepDetailWarning()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

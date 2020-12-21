# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_browser_error import SyntheticsBrowserError
from datadog_api_client.v1.model.synthetics_check_type import SyntheticsCheckType
from datadog_api_client.v1.model.synthetics_playing_tab import SyntheticsPlayingTab
from datadog_api_client.v1.model.synthetics_step_detail_warnings import SyntheticsStepDetailWarnings
from datadog_api_client.v1.model.synthetics_step_type import SyntheticsStepType
globals()['SyntheticsBrowserError'] = SyntheticsBrowserError
globals()['SyntheticsCheckType'] = SyntheticsCheckType
globals()['SyntheticsPlayingTab'] = SyntheticsPlayingTab
globals()['SyntheticsStepDetailWarnings'] = SyntheticsStepDetailWarnings
globals()['SyntheticsStepType'] = SyntheticsStepType
from datadog_api_client.v1.model.synthetics_step_detail import SyntheticsStepDetail


class TestSyntheticsStepDetail(unittest.TestCase):
    """SyntheticsStepDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsStepDetail(self):
        """Test SyntheticsStepDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsStepDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

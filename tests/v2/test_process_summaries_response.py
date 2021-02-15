# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.process_summaries_meta import ProcessSummariesMeta
from datadog_api_client.v2.model.process_summary import ProcessSummary

globals()["ProcessSummariesMeta"] = ProcessSummariesMeta
globals()["ProcessSummary"] = ProcessSummary
from datadog_api_client.v2.model.process_summaries_response import ProcessSummariesResponse


class TestProcessSummariesResponse(unittest.TestCase):
    """ProcessSummariesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProcessSummariesResponse(self):
        """Test ProcessSummariesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProcessSummariesResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

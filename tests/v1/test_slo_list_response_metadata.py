# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_list_response_metadata_page import SLOListResponseMetadataPage

globals()["SLOListResponseMetadataPage"] = SLOListResponseMetadataPage
from datadog_api_client.v1.model.slo_list_response_metadata import SLOListResponseMetadata


class TestSLOListResponseMetadata(unittest.TestCase):
    """SLOListResponseMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOListResponseMetadata(self):
        """Test SLOListResponseMetadata"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOListResponseMetadata()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

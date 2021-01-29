# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.aws_tag_filter_list_response_filters import AWSTagFilterListResponseFilters

globals()["AWSTagFilterListResponseFilters"] = AWSTagFilterListResponseFilters
from datadog_api_client.v1.model.aws_tag_filter_list_response import AWSTagFilterListResponse


class TestAWSTagFilterListResponse(unittest.TestCase):
    """AWSTagFilterListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAWSTagFilterListResponse(self):
        """Test AWSTagFilterListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AWSTagFilterListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

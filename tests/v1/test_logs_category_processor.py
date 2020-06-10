# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import logs_category_processor_categories
except ImportError:
    logs_category_processor_categories = sys.modules[
        'datadog_api_client.v1.model.logs_category_processor_categories']
try:
    from datadog_api_client.v1.model import logs_category_processor_type
except ImportError:
    logs_category_processor_type = sys.modules[
        'datadog_api_client.v1.model.logs_category_processor_type']
from datadog_api_client.v1.model.logs_category_processor import LogsCategoryProcessor


class TestLogsCategoryProcessor(unittest.TestCase):
    """LogsCategoryProcessor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsCategoryProcessor(self):
        """Test LogsCategoryProcessor"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsCategoryProcessor()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

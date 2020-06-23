# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import service_level_objective
except ImportError:
    service_level_objective = sys.modules[
        'datadog_api_client.v1.model.service_level_objective']
from datadog_api_client.v1.model.slo_response import SLOResponse


class TestSLOResponse(unittest.TestCase):
    """SLOResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOResponse(self):
        """Test SLOResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

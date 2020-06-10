# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import creator
except ImportError:
    creator = sys.modules[
        'datadog_api_client.v1.model.creator']
try:
    from datadog_api_client.v1.model import service_level_objective_query
except ImportError:
    service_level_objective_query = sys.modules[
        'datadog_api_client.v1.model.service_level_objective_query']
try:
    from datadog_api_client.v1.model import slo_threshold
except ImportError:
    slo_threshold = sys.modules[
        'datadog_api_client.v1.model.slo_threshold']
try:
    from datadog_api_client.v1.model import slo_type
except ImportError:
    slo_type = sys.modules[
        'datadog_api_client.v1.model.slo_type']
from datadog_api_client.v1.model.service_level_objective import ServiceLevelObjective


class TestServiceLevelObjective(unittest.TestCase):
    """ServiceLevelObjective unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceLevelObjective(self):
        """Test ServiceLevelObjective"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceLevelObjective()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

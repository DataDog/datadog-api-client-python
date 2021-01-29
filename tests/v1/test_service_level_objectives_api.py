# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi  # noqa: E501


class TestServiceLevelObjectivesApi(unittest.TestCase):
    """ServiceLevelObjectivesApi unit test stubs"""

    def setUp(self):
        self.api = ServiceLevelObjectivesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_can_delete_slo(self):
        """Test case for check_can_delete_slo

        Check if SLOs can be safely deleted  # noqa: E501
        """
        pass

    def test_create_slo(self):
        """Test case for create_slo

        Create a SLO object  # noqa: E501
        """
        pass

    def test_delete_slo(self):
        """Test case for delete_slo

        Delete a SLO  # noqa: E501
        """
        pass

    def test_delete_slo_timeframe_in_bulk(self):
        """Test case for delete_slo_timeframe_in_bulk

        Bulk Delete SLO Timeframes  # noqa: E501
        """
        pass

    def test_get_slo(self):
        """Test case for get_slo

        Get a SLO's details  # noqa: E501
        """
        pass

    def test_get_slo_history(self):
        """Test case for get_slo_history

        Get an SLO's history  # noqa: E501
        """
        pass

    def test_list_sl_os(self):
        """Test case for list_sl_os

        Search SLOs  # noqa: E501
        """
        pass

    def test_update_slo(self):
        """Test case for update_slo

        Update a SLO  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

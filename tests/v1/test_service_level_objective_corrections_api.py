# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.service_level_objective_corrections_api import (
    ServiceLevelObjectiveCorrectionsApi,
)  # noqa: E501


class TestServiceLevelObjectiveCorrectionsApi(unittest.TestCase):
    """ServiceLevelObjectiveCorrectionsApi unit test stubs"""

    def setUp(self):
        self.api = ServiceLevelObjectiveCorrectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_slo_correction(self):
        """Test case for create_slo_correction

        Create an SLO correction  # noqa: E501
        """
        pass

    def test_delete_slo_correction(self):
        """Test case for delete_slo_correction

        Delete an SLO Correction  # noqa: E501
        """
        pass

    def test_get_slo_correction(self):
        """Test case for get_slo_correction

        Get an SLO correction for an SLO  # noqa: E501
        """
        pass

    def test_list_slo_correction(self):
        """Test case for list_slo_correction

        Get all SLO corrections  # noqa: E501
        """
        pass

    def test_update_slo_correction(self):
        """Test case for update_slo_correction

        Update an SLO Correction  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

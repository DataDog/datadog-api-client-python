# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_get_request_data import (
        TestOptimizationFlakyTestsManagementPoliciesGetRequestData,
    )


class TestOptimizationFlakyTestsManagementPoliciesGetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_get_request_data import (
            TestOptimizationFlakyTestsManagementPoliciesGetRequestData,
        )

        return {
            "data": (TestOptimizationFlakyTestsManagementPoliciesGetRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TestOptimizationFlakyTestsManagementPoliciesGetRequestData, **kwargs):
        """
        Request object for getting Flaky Tests Management policies.

        :param data: Data object for get Flaky Tests Management policies request.
        :type data: TestOptimizationFlakyTestsManagementPoliciesGetRequestData
        """
        super().__init__(kwargs)

        self_.data = data

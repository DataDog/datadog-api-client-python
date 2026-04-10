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
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_update_request_data import (
        TestOptimizationFlakyTestsManagementPoliciesUpdateRequestData,
    )


class TestOptimizationFlakyTestsManagementPoliciesUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_update_request_data import (
            TestOptimizationFlakyTestsManagementPoliciesUpdateRequestData,
        )

        return {
            "data": (TestOptimizationFlakyTestsManagementPoliciesUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TestOptimizationFlakyTestsManagementPoliciesUpdateRequestData, **kwargs):
        """
        Request object for updating Flaky Tests Management policies.

        :param data: Data object for update Flaky Tests Management policies request.
        :type data: TestOptimizationFlakyTestsManagementPoliciesUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data

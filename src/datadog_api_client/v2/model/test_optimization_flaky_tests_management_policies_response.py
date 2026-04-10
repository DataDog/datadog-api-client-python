# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_data import (
        TestOptimizationFlakyTestsManagementPoliciesData,
    )


class TestOptimizationFlakyTestsManagementPoliciesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_data import (
            TestOptimizationFlakyTestsManagementPoliciesData,
        )

        return {
            "data": (TestOptimizationFlakyTestsManagementPoliciesData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[TestOptimizationFlakyTestsManagementPoliciesData, UnsetType] = unset, **kwargs):
        """
        Response object containing Flaky Tests Management policies for a repository.

        :param data: Data object for Flaky Tests Management policies response.
        :type data: TestOptimizationFlakyTestsManagementPoliciesData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)

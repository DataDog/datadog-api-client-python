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
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_get_request_attributes import (
        TestOptimizationFlakyTestsManagementPoliciesGetRequestAttributes,
    )
    from datadog_api_client.v2.model.test_optimization_get_flaky_tests_management_policies_request_data_type import (
        TestOptimizationGetFlakyTestsManagementPoliciesRequestDataType,
    )


class TestOptimizationFlakyTestsManagementPoliciesGetRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_get_request_attributes import (
            TestOptimizationFlakyTestsManagementPoliciesGetRequestAttributes,
        )
        from datadog_api_client.v2.model.test_optimization_get_flaky_tests_management_policies_request_data_type import (
            TestOptimizationGetFlakyTestsManagementPoliciesRequestDataType,
        )

        return {
            "attributes": (TestOptimizationFlakyTestsManagementPoliciesGetRequestAttributes,),
            "type": (TestOptimizationGetFlakyTestsManagementPoliciesRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TestOptimizationFlakyTestsManagementPoliciesGetRequestAttributes,
        type: TestOptimizationGetFlakyTestsManagementPoliciesRequestDataType,
        **kwargs,
    ):
        """
        Data object for get Flaky Tests Management policies request.

        :param attributes: Attributes for requesting Flaky Tests Management policies.
        :type attributes: TestOptimizationFlakyTestsManagementPoliciesGetRequestAttributes

        :param type: JSON:API type for get Flaky Tests Management policies request.
            The value must always be ``test_optimization_get_flaky_tests_management_policies_request``.
        :type type: TestOptimizationGetFlakyTestsManagementPoliciesRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

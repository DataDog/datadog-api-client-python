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
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_update_request_attributes import (
        TestOptimizationFlakyTestsManagementPoliciesUpdateRequestAttributes,
    )
    from datadog_api_client.v2.model.test_optimization_update_flaky_tests_management_policies_request_data_type import (
        TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType,
    )


class TestOptimizationFlakyTestsManagementPoliciesUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_update_request_attributes import (
            TestOptimizationFlakyTestsManagementPoliciesUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.test_optimization_update_flaky_tests_management_policies_request_data_type import (
            TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType,
        )

        return {
            "attributes": (TestOptimizationFlakyTestsManagementPoliciesUpdateRequestAttributes,),
            "type": (TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TestOptimizationFlakyTestsManagementPoliciesUpdateRequestAttributes,
        type: TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType,
        **kwargs,
    ):
        """
        Data object for update Flaky Tests Management policies request.

        :param attributes: Attributes for updating Flaky Tests Management policies.
            Only provided policy blocks are updated; omitted blocks are left unchanged.
        :type attributes: TestOptimizationFlakyTestsManagementPoliciesUpdateRequestAttributes

        :param type: JSON:API type for update Flaky Tests Management policies request.
            The value must always be ``test_optimization_update_flaky_tests_management_policies_request``.
        :type type: TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

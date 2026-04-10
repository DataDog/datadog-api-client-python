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
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_attributes import (
        TestOptimizationFlakyTestsManagementPoliciesAttributes,
    )
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_type import (
        TestOptimizationFlakyTestsManagementPoliciesType,
    )


class TestOptimizationFlakyTestsManagementPoliciesData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_attributes import (
            TestOptimizationFlakyTestsManagementPoliciesAttributes,
        )
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_type import (
            TestOptimizationFlakyTestsManagementPoliciesType,
        )

        return {
            "attributes": (TestOptimizationFlakyTestsManagementPoliciesAttributes,),
            "id": (str,),
            "type": (TestOptimizationFlakyTestsManagementPoliciesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[TestOptimizationFlakyTestsManagementPoliciesAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[TestOptimizationFlakyTestsManagementPoliciesType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for Flaky Tests Management policies response.

        :param attributes: Attributes of the Flaky Tests Management policies for a repository.
        :type attributes: TestOptimizationFlakyTestsManagementPoliciesAttributes, optional

        :param id: The repository identifier used as the resource ID.
        :type id: str, optional

        :param type: JSON:API type for Flaky Tests Management policies response.
            The value must always be ``test_optimization_flaky_tests_management_policies``.
        :type type: TestOptimizationFlakyTestsManagementPoliciesType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

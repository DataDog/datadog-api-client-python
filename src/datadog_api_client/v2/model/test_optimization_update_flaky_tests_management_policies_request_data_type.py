# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType(ModelSimple):
    """
    JSON:API type for update Flaky Tests Management policies request.
        The value must always be `test_optimization_update_flaky_tests_management_policies_request`.

    :param value: If omitted defaults to "test_optimization_update_flaky_tests_management_policies_request". Must be one of ["test_optimization_update_flaky_tests_management_policies_request"].
    :type value: str
    """

    allowed_values = {
        "test_optimization_update_flaky_tests_management_policies_request",
    }
    TEST_OPTIMIZATION_UPDATE_FLAKY_TESTS_MANAGEMENT_POLICIES_REQUEST: ClassVar[
        "TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType"
    ]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType.TEST_OPTIMIZATION_UPDATE_FLAKY_TESTS_MANAGEMENT_POLICIES_REQUEST = TestOptimizationUpdateFlakyTestsManagementPoliciesRequestDataType(
    "test_optimization_update_flaky_tests_management_policies_request"
)

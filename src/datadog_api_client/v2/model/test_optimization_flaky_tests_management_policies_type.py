# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TestOptimizationFlakyTestsManagementPoliciesType(ModelSimple):
    """
    JSON:API type for Flaky Tests Management policies response.
        The value must always be `test_optimization_flaky_tests_management_policies`.

    :param value: If omitted defaults to "test_optimization_flaky_tests_management_policies". Must be one of ["test_optimization_flaky_tests_management_policies"].
    :type value: str
    """

    allowed_values = {
        "test_optimization_flaky_tests_management_policies",
    }
    TEST_OPTIMIZATION_FLAKY_TESTS_MANAGEMENT_POLICIES: ClassVar["TestOptimizationFlakyTestsManagementPoliciesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TestOptimizationFlakyTestsManagementPoliciesType.TEST_OPTIMIZATION_FLAKY_TESTS_MANAGEMENT_POLICIES = (
    TestOptimizationFlakyTestsManagementPoliciesType("test_optimization_flaky_tests_management_policies")
)

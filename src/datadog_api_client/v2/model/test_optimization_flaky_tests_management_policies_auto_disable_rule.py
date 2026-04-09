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
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_disabled_status import (
        TestOptimizationFlakyTestsManagementPoliciesDisabledStatus,
    )


class TestOptimizationFlakyTestsManagementPoliciesAutoDisableRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_disabled_status import (
            TestOptimizationFlakyTestsManagementPoliciesDisabledStatus,
        )

        return {
            "enabled": (bool,),
            "status": (TestOptimizationFlakyTestsManagementPoliciesDisabledStatus,),
            "window_seconds": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "status": "status",
        "window_seconds": "window_seconds",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        status: Union[TestOptimizationFlakyTestsManagementPoliciesDisabledStatus, UnsetType] = unset,
        window_seconds: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Automatic disable triggering rule based on a time window and test status.

        :param enabled: Whether this auto-disable rule is enabled.
        :type enabled: bool, optional

        :param status: Test status that the disable policy applies to.
            Must be either ``active`` or ``quarantined``.
        :type status: TestOptimizationFlakyTestsManagementPoliciesDisabledStatus, optional

        :param window_seconds: Time window in seconds over which flakiness is evaluated. Must be greater than 0.
        :type window_seconds: int, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if status is not unset:
            kwargs["status"] = status
        if window_seconds is not unset:
            kwargs["window_seconds"] = window_seconds
        super().__init__(kwargs)

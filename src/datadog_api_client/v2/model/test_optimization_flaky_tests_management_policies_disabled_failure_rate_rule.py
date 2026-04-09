# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

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


class TestOptimizationFlakyTestsManagementPoliciesDisabledFailureRateRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_disabled_status import (
            TestOptimizationFlakyTestsManagementPoliciesDisabledStatus,
        )

        return {
            "branches": ([str],),
            "enabled": (bool,),
            "min_runs": (int,),
            "status": (TestOptimizationFlakyTestsManagementPoliciesDisabledStatus,),
            "threshold": (float,),
        }

    attribute_map = {
        "branches": "branches",
        "enabled": "enabled",
        "min_runs": "min_runs",
        "status": "status",
        "threshold": "threshold",
    }

    def __init__(
        self_,
        branches: Union[List[str], UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        min_runs: Union[int, UnsetType] = unset,
        status: Union[TestOptimizationFlakyTestsManagementPoliciesDisabledStatus, UnsetType] = unset,
        threshold: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Failure-rate-based rule for the disabled policy.

        :param branches: List of branches to which this rule applies.
        :type branches: [str], optional

        :param enabled: Whether this failure rate rule is enabled.
        :type enabled: bool, optional

        :param min_runs: Minimum number of runs required before the rule is evaluated. Must be greater than or equal to 0.
        :type min_runs: int, optional

        :param status: Test status that the disable policy applies to.
            Must be either ``active`` or ``quarantined``.
        :type status: TestOptimizationFlakyTestsManagementPoliciesDisabledStatus, optional

        :param threshold: Failure rate threshold (0.0–1.0) above which the rule triggers.
        :type threshold: float, optional
        """
        if branches is not unset:
            kwargs["branches"] = branches
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if min_runs is not unset:
            kwargs["min_runs"] = min_runs
        if status is not unset:
            kwargs["status"] = status
        if threshold is not unset:
            kwargs["threshold"] = threshold
        super().__init__(kwargs)

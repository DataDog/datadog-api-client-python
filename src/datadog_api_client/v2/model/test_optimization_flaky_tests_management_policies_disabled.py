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
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_auto_disable_rule import (
        TestOptimizationFlakyTestsManagementPoliciesAutoDisableRule,
    )
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_branch_rule import (
        TestOptimizationFlakyTestsManagementPoliciesBranchRule,
    )
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_disabled_failure_rate_rule import (
        TestOptimizationFlakyTestsManagementPoliciesDisabledFailureRateRule,
    )


class TestOptimizationFlakyTestsManagementPoliciesDisabled(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_auto_disable_rule import (
            TestOptimizationFlakyTestsManagementPoliciesAutoDisableRule,
        )
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_branch_rule import (
            TestOptimizationFlakyTestsManagementPoliciesBranchRule,
        )
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_disabled_failure_rate_rule import (
            TestOptimizationFlakyTestsManagementPoliciesDisabledFailureRateRule,
        )

        return {
            "auto_disable_rule": (TestOptimizationFlakyTestsManagementPoliciesAutoDisableRule,),
            "branch_rule": (TestOptimizationFlakyTestsManagementPoliciesBranchRule,),
            "enabled": (bool,),
            "failure_rate_rule": (TestOptimizationFlakyTestsManagementPoliciesDisabledFailureRateRule,),
        }

    attribute_map = {
        "auto_disable_rule": "auto_disable_rule",
        "branch_rule": "branch_rule",
        "enabled": "enabled",
        "failure_rate_rule": "failure_rate_rule",
    }

    def __init__(
        self_,
        auto_disable_rule: Union[TestOptimizationFlakyTestsManagementPoliciesAutoDisableRule, UnsetType] = unset,
        branch_rule: Union[TestOptimizationFlakyTestsManagementPoliciesBranchRule, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        failure_rate_rule: Union[
            TestOptimizationFlakyTestsManagementPoliciesDisabledFailureRateRule, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Configuration for the disabled Flaky Tests Management policy.

        :param auto_disable_rule: Automatic disable triggering rule based on a time window and test status.
        :type auto_disable_rule: TestOptimizationFlakyTestsManagementPoliciesAutoDisableRule, optional

        :param branch_rule: Branch filtering rule for a Flaky Tests Management policy.
        :type branch_rule: TestOptimizationFlakyTestsManagementPoliciesBranchRule, optional

        :param enabled: Whether the disabled policy is enabled.
        :type enabled: bool, optional

        :param failure_rate_rule: Failure-rate-based rule for the disabled policy.
        :type failure_rate_rule: TestOptimizationFlakyTestsManagementPoliciesDisabledFailureRateRule, optional
        """
        if auto_disable_rule is not unset:
            kwargs["auto_disable_rule"] = auto_disable_rule
        if branch_rule is not unset:
            kwargs["branch_rule"] = branch_rule
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if failure_rate_rule is not unset:
            kwargs["failure_rate_rule"] = failure_rate_rule
        super().__init__(kwargs)

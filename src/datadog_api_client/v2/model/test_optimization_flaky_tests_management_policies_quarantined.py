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
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_auto_quarantine_rule import (
        TestOptimizationFlakyTestsManagementPoliciesAutoQuarantineRule,
    )
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_branch_rule import (
        TestOptimizationFlakyTestsManagementPoliciesBranchRule,
    )
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_quarantined_failure_rate_rule import (
        TestOptimizationFlakyTestsManagementPoliciesQuarantinedFailureRateRule,
    )


class TestOptimizationFlakyTestsManagementPoliciesQuarantined(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_auto_quarantine_rule import (
            TestOptimizationFlakyTestsManagementPoliciesAutoQuarantineRule,
        )
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_branch_rule import (
            TestOptimizationFlakyTestsManagementPoliciesBranchRule,
        )
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_quarantined_failure_rate_rule import (
            TestOptimizationFlakyTestsManagementPoliciesQuarantinedFailureRateRule,
        )

        return {
            "auto_quarantine_rule": (TestOptimizationFlakyTestsManagementPoliciesAutoQuarantineRule,),
            "branch_rule": (TestOptimizationFlakyTestsManagementPoliciesBranchRule,),
            "enabled": (bool,),
            "failure_rate_rule": (TestOptimizationFlakyTestsManagementPoliciesQuarantinedFailureRateRule,),
        }

    attribute_map = {
        "auto_quarantine_rule": "auto_quarantine_rule",
        "branch_rule": "branch_rule",
        "enabled": "enabled",
        "failure_rate_rule": "failure_rate_rule",
    }

    def __init__(
        self_,
        auto_quarantine_rule: Union[TestOptimizationFlakyTestsManagementPoliciesAutoQuarantineRule, UnsetType] = unset,
        branch_rule: Union[TestOptimizationFlakyTestsManagementPoliciesBranchRule, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        failure_rate_rule: Union[
            TestOptimizationFlakyTestsManagementPoliciesQuarantinedFailureRateRule, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Configuration for the quarantined Flaky Tests Management policy.

        :param auto_quarantine_rule: Automatic quarantine triggering rule based on a time window.
        :type auto_quarantine_rule: TestOptimizationFlakyTestsManagementPoliciesAutoQuarantineRule, optional

        :param branch_rule: Branch filtering rule for a Flaky Tests Management policy.
        :type branch_rule: TestOptimizationFlakyTestsManagementPoliciesBranchRule, optional

        :param enabled: Whether the quarantined policy is enabled.
        :type enabled: bool, optional

        :param failure_rate_rule: Failure-rate-based rule for the quarantined policy.
        :type failure_rate_rule: TestOptimizationFlakyTestsManagementPoliciesQuarantinedFailureRateRule, optional
        """
        if auto_quarantine_rule is not unset:
            kwargs["auto_quarantine_rule"] = auto_quarantine_rule
        if branch_rule is not unset:
            kwargs["branch_rule"] = branch_rule
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if failure_rate_rule is not unset:
            kwargs["failure_rate_rule"] = failure_rate_rule
        super().__init__(kwargs)

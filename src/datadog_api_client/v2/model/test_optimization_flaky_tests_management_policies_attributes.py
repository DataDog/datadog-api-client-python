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
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_attempt_to_fix import (
        TestOptimizationFlakyTestsManagementPoliciesAttemptToFix,
    )
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_disabled import (
        TestOptimizationFlakyTestsManagementPoliciesDisabled,
    )
    from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_quarantined import (
        TestOptimizationFlakyTestsManagementPoliciesQuarantined,
    )


class TestOptimizationFlakyTestsManagementPoliciesAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_attempt_to_fix import (
            TestOptimizationFlakyTestsManagementPoliciesAttemptToFix,
        )
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_disabled import (
            TestOptimizationFlakyTestsManagementPoliciesDisabled,
        )
        from datadog_api_client.v2.model.test_optimization_flaky_tests_management_policies_quarantined import (
            TestOptimizationFlakyTestsManagementPoliciesQuarantined,
        )

        return {
            "attempt_to_fix": (TestOptimizationFlakyTestsManagementPoliciesAttemptToFix,),
            "disabled": (TestOptimizationFlakyTestsManagementPoliciesDisabled,),
            "quarantined": (TestOptimizationFlakyTestsManagementPoliciesQuarantined,),
            "repository_id": (str,),
        }

    attribute_map = {
        "attempt_to_fix": "attempt_to_fix",
        "disabled": "disabled",
        "quarantined": "quarantined",
        "repository_id": "repository_id",
    }

    def __init__(
        self_,
        attempt_to_fix: Union[TestOptimizationFlakyTestsManagementPoliciesAttemptToFix, UnsetType] = unset,
        disabled: Union[TestOptimizationFlakyTestsManagementPoliciesDisabled, UnsetType] = unset,
        quarantined: Union[TestOptimizationFlakyTestsManagementPoliciesQuarantined, UnsetType] = unset,
        repository_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the Flaky Tests Management policies for a repository.

        :param attempt_to_fix: Configuration for the attempt-to-fix Flaky Tests Management policy.
        :type attempt_to_fix: TestOptimizationFlakyTestsManagementPoliciesAttemptToFix, optional

        :param disabled: Configuration for the disabled Flaky Tests Management policy.
        :type disabled: TestOptimizationFlakyTestsManagementPoliciesDisabled, optional

        :param quarantined: Configuration for the quarantined Flaky Tests Management policy.
        :type quarantined: TestOptimizationFlakyTestsManagementPoliciesQuarantined, optional

        :param repository_id: The repository identifier.
        :type repository_id: str, optional
        """
        if attempt_to_fix is not unset:
            kwargs["attempt_to_fix"] = attempt_to_fix
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if quarantined is not unset:
            kwargs["quarantined"] = quarantined
        if repository_id is not unset:
            kwargs["repository_id"] = repository_id
        super().__init__(kwargs)

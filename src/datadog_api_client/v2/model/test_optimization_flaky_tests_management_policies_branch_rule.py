# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TestOptimizationFlakyTestsManagementPoliciesBranchRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "branches": ([str],),
            "enabled": (bool,),
            "excluded_branches": ([str],),
            "excluded_test_services": ([str],),
        }

    attribute_map = {
        "branches": "branches",
        "enabled": "enabled",
        "excluded_branches": "excluded_branches",
        "excluded_test_services": "excluded_test_services",
    }

    def __init__(
        self_,
        branches: Union[List[str], UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        excluded_branches: Union[List[str], UnsetType] = unset,
        excluded_test_services: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Branch filtering rule for a Flaky Tests Management policy.

        :param branches: List of branches to which the policy applies.
        :type branches: [str], optional

        :param enabled: Whether this branch rule is enabled.
        :type enabled: bool, optional

        :param excluded_branches: List of branches excluded from the policy.
        :type excluded_branches: [str], optional

        :param excluded_test_services: List of test services excluded from the policy.
        :type excluded_test_services: [str], optional
        """
        if branches is not unset:
            kwargs["branches"] = branches
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if excluded_branches is not unset:
            kwargs["excluded_branches"] = excluded_branches
        if excluded_test_services is not unset:
            kwargs["excluded_test_services"] = excluded_test_services
        super().__init__(kwargs)

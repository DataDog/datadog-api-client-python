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


class TestOptimizationFlakyTestsManagementPoliciesQuarantinedFailureRateRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "branches": ([str],),
            "enabled": (bool,),
            "min_runs": (int,),
            "threshold": (float,),
        }

    attribute_map = {
        "branches": "branches",
        "enabled": "enabled",
        "min_runs": "min_runs",
        "threshold": "threshold",
    }

    def __init__(
        self_,
        branches: Union[List[str], UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        min_runs: Union[int, UnsetType] = unset,
        threshold: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Failure-rate-based rule for the quarantined policy.

        :param branches: List of branches to which this rule applies.
        :type branches: [str], optional

        :param enabled: Whether this failure rate rule is enabled.
        :type enabled: bool, optional

        :param min_runs: Minimum number of runs required before the rule is evaluated. Must be greater than or equal to 0.
        :type min_runs: int, optional

        :param threshold: Failure rate threshold (0.0–1.0) above which the rule triggers.
        :type threshold: float, optional
        """
        if branches is not unset:
            kwargs["branches"] = branches
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if min_runs is not unset:
            kwargs["min_runs"] = min_runs
        if threshold is not unset:
            kwargs["threshold"] = threshold
        super().__init__(kwargs)

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.flaky_test_history_policy_meta_config import FlakyTestHistoryPolicyMetaConfig


class FlakyTestHistoryPolicyMeta(ModelNormal):
    validations = {
        "days_active": {
            "inclusive_maximum": 2147483647,
        },
        "days_without_flake": {
            "inclusive_maximum": 2147483647,
        },
        "failure_rate": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
        "total_runs": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.flaky_test_history_policy_meta_config import FlakyTestHistoryPolicyMetaConfig

        return {
            "branches": ([str], none_type),
            "config": (FlakyTestHistoryPolicyMetaConfig,),
            "days_active": (int, none_type),
            "days_without_flake": (int, none_type),
            "failure_rate": (float, none_type),
            "state": (str, none_type),
            "total_runs": (int, none_type),
        }

    attribute_map = {
        "branches": "branches",
        "config": "config",
        "days_active": "days_active",
        "days_without_flake": "days_without_flake",
        "failure_rate": "failure_rate",
        "state": "state",
        "total_runs": "total_runs",
    }

    def __init__(
        self_,
        branches: Union[List[str], none_type, UnsetType] = unset,
        config: Union[FlakyTestHistoryPolicyMetaConfig, UnsetType] = unset,
        days_active: Union[int, none_type, UnsetType] = unset,
        days_without_flake: Union[int, none_type, UnsetType] = unset,
        failure_rate: Union[float, none_type, UnsetType] = unset,
        state: Union[str, none_type, UnsetType] = unset,
        total_runs: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the policy that triggered this status change.

        :param branches: Branches where the test was flaky at the time of the status change.
        :type branches: [str], none_type, optional

        :param config: Configuration parameters of the policy that triggered this status change.
        :type config: FlakyTestHistoryPolicyMetaConfig, optional

        :param days_active: The number of days the test has been active at the time of the status change.
        :type days_active: int, none_type, optional

        :param days_without_flake: The number of days since the test last exhibited flakiness.
        :type days_without_flake: int, none_type, optional

        :param failure_rate: The failure rate of the test at the time of the status change.
        :type failure_rate: float, none_type, optional

        :param state: The previous state of the test.
        :type state: str, none_type, optional

        :param total_runs: The total number of test runs at the time of the status change.
        :type total_runs: int, none_type, optional
        """
        if branches is not unset:
            kwargs["branches"] = branches
        if config is not unset:
            kwargs["config"] = config
        if days_active is not unset:
            kwargs["days_active"] = days_active
        if days_without_flake is not unset:
            kwargs["days_without_flake"] = days_without_flake
        if failure_rate is not unset:
            kwargs["failure_rate"] = failure_rate
        if state is not unset:
            kwargs["state"] = state
        if total_runs is not unset:
            kwargs["total_runs"] = total_runs
        super().__init__(kwargs)

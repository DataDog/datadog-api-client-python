# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class FlakyTestHistoryPolicyMetaConfig(ModelNormal):
    validations = {
        "days_active": {
            "inclusive_maximum": 2147483647,
        },
        "failure_rate": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
        "required_runs": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "branches": ([str], none_type),
            "days_active": (int, none_type),
            "failure_rate": (float, none_type),
            "forget_branches": ([str], none_type),
            "required_runs": (int, none_type),
            "state": (str, none_type),
            "test_services": ([str], none_type),
        }

    attribute_map = {
        "branches": "branches",
        "days_active": "days_active",
        "failure_rate": "failure_rate",
        "forget_branches": "forget_branches",
        "required_runs": "required_runs",
        "state": "state",
        "test_services": "test_services",
    }

    def __init__(
        self_,
        branches: Union[List[str], none_type, UnsetType] = unset,
        days_active: Union[int, none_type, UnsetType] = unset,
        failure_rate: Union[float, none_type, UnsetType] = unset,
        forget_branches: Union[List[str], none_type, UnsetType] = unset,
        required_runs: Union[int, none_type, UnsetType] = unset,
        state: Union[str, none_type, UnsetType] = unset,
        test_services: Union[List[str], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration parameters of the policy that triggered this status change.

        :param branches: The branches considered by the policy.
        :type branches: [str], none_type, optional

        :param days_active: The number of days a test must have been active for the policy to trigger.
        :type days_active: int, none_type, optional

        :param failure_rate: The failure rate threshold for the policy to trigger.
        :type failure_rate: float, none_type, optional

        :param forget_branches: Branches excluded from the policy evaluation.
        :type forget_branches: [str], none_type, optional

        :param required_runs: The minimum number of test runs required for the policy to trigger.
        :type required_runs: int, none_type, optional

        :param state: The target state the policy transitions the test from.
        :type state: str, none_type, optional

        :param test_services: Test services excluded from the policy evaluation.
        :type test_services: [str], none_type, optional
        """
        if branches is not unset:
            kwargs["branches"] = branches
        if days_active is not unset:
            kwargs["days_active"] = days_active
        if failure_rate is not unset:
            kwargs["failure_rate"] = failure_rate
        if forget_branches is not unset:
            kwargs["forget_branches"] = forget_branches
        if required_runs is not unset:
            kwargs["required_runs"] = required_runs
        if state is not unset:
            kwargs["state"] = state
        if test_services is not unset:
            kwargs["test_services"] = test_services
        super().__init__(kwargs)

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DeploymentRuleOptionsMonitor(ModelNormal):
    validations = {
        "warmup": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "duration": (int,),
            "fail_on_no_data": (bool,),
            "fail_on_no_groups_found": (bool,),
            "query": (str,),
            "warmup": (int,),
        }

    attribute_map = {
        "duration": "duration",
        "fail_on_no_data": "fail_on_no_data",
        "fail_on_no_groups_found": "fail_on_no_groups_found",
        "query": "query",
        "warmup": "warmup",
    }

    def __init__(
        self_,
        query: str,
        duration: Union[int, UnsetType] = unset,
        fail_on_no_data: Union[bool, UnsetType] = unset,
        fail_on_no_groups_found: Union[bool, UnsetType] = unset,
        warmup: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Monitor options for deployment rules.

        :param duration: Seconds the monitor needs to stay in OK status for the rule to pass.
        :type duration: int, optional

        :param fail_on_no_data: Whether the rule should fail if a matching monitor group is in a NO DATA state.
        :type fail_on_no_data: bool, optional

        :param fail_on_no_groups_found: Whether the rule should fail if no monitor groups are found for the query.
        :type fail_on_no_groups_found: bool, optional

        :param query: Monitors that match this query are evaluated.
        :type query: str

        :param warmup: Seconds to wait after a deployment starts before evaluating the monitor's status.
        :type warmup: int, optional
        """
        if duration is not unset:
            kwargs["duration"] = duration
        if fail_on_no_data is not unset:
            kwargs["fail_on_no_data"] = fail_on_no_data
        if fail_on_no_groups_found is not unset:
            kwargs["fail_on_no_groups_found"] = fail_on_no_groups_found
        if warmup is not unset:
            kwargs["warmup"] = warmup
        super().__init__(kwargs)

        self_.query = query

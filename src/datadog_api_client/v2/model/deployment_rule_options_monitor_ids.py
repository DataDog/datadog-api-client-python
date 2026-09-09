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
    from datadog_api_client.v2.model.deployment_rule_options_monitor_id import DeploymentRuleOptionsMonitorId


class DeploymentRuleOptionsMonitorIds(ModelNormal):
    validations = {
        "monitor_ids": {
            "min_items": 1,
        },
        "warmup": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_rule_options_monitor_id import DeploymentRuleOptionsMonitorId

        return {
            "duration": (int,),
            "fail_on_no_data": (bool,),
            "fail_on_no_groups_found": (bool,),
            "monitor_ids": ([DeploymentRuleOptionsMonitorId],),
            "warmup": (int,),
        }

    attribute_map = {
        "duration": "duration",
        "fail_on_no_data": "fail_on_no_data",
        "fail_on_no_groups_found": "fail_on_no_groups_found",
        "monitor_ids": "monitor_ids",
        "warmup": "warmup",
    }

    def __init__(
        self_,
        monitor_ids: List[DeploymentRuleOptionsMonitorId],
        duration: Union[int, UnsetType] = unset,
        fail_on_no_data: Union[bool, UnsetType] = unset,
        fail_on_no_groups_found: Union[bool, UnsetType] = unset,
        warmup: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Specific monitor options for deployment rules.

        :param duration: Seconds the monitors need to stay in OK status for the rule to pass.
        :type duration: int, optional

        :param fail_on_no_data: Whether the rule should fail if a selected monitor group is in a NO DATA state.
        :type fail_on_no_data: bool, optional

        :param fail_on_no_groups_found: Whether the rule should fail if no monitor groups are found for the selected monitors.
        :type fail_on_no_groups_found: bool, optional

        :param monitor_ids: A non-empty list of specific monitors to evaluate.
        :type monitor_ids: [DeploymentRuleOptionsMonitorId]

        :param warmup: Seconds to wait after a deployment starts before evaluating the monitors' statuses.
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

        self_.monitor_ids = monitor_ids

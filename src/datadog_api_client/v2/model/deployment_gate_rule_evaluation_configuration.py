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


class DeploymentGateRuleEvaluationConfiguration(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "allowed_resources": ([str],),
            "duration": (int,),
            "excluded_resources": ([str],),
            "fail_on_no_data": (bool,),
            "fail_on_no_groups_found": (bool,),
            "monitor_ids": ([str],),
            "query": (str,),
            "warmup": (int,),
        }

    attribute_map = {
        "allowed_resources": "allowed_resources",
        "duration": "duration",
        "excluded_resources": "excluded_resources",
        "fail_on_no_data": "fail_on_no_data",
        "fail_on_no_groups_found": "fail_on_no_groups_found",
        "monitor_ids": "monitor_ids",
        "query": "query",
        "warmup": "warmup",
    }

    def __init__(
        self_,
        allowed_resources: Union[List[str], UnsetType] = unset,
        duration: Union[int, UnsetType] = unset,
        excluded_resources: Union[List[str], UnsetType] = unset,
        fail_on_no_data: Union[bool, UnsetType] = unset,
        fail_on_no_groups_found: Union[bool, UnsetType] = unset,
        monitor_ids: Union[List[str], UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        warmup: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Evaluated rule configuration. Fields depend on rule type and unset fields are omitted.
        Monitor rules can include ``duration`` , ``query`` , ``monitor_ids`` , ``warmup`` , ``fail_on_no_groups_found`` , and ``fail_on_no_data``.
        Faulty deployment detection rules can include ``duration`` , ``allowed_resources`` , and ``excluded_resources``.

        :param allowed_resources: APM resources explicitly allowed by faulty deployment detection.
        :type allowed_resources: [str], optional

        :param duration: Evaluation duration configured for this rule.
        :type duration: int, optional

        :param excluded_resources: APM resources excluded from faulty deployment detection.
        :type excluded_resources: [str], optional

        :param fail_on_no_data: Whether a monitor rule fails when no data is found.
        :type fail_on_no_data: bool, optional

        :param fail_on_no_groups_found: Whether a monitor rule fails when no groups are found.
        :type fail_on_no_groups_found: bool, optional

        :param monitor_ids: Monitor IDs evaluated by a monitor rule.
        :type monitor_ids: [str], optional

        :param query: Monitor query used by a monitor rule.
        :type query: str, optional

        :param warmup: Warm-up duration in seconds for a monitor rule. Omitted when zero.
        :type warmup: int, optional
        """
        if allowed_resources is not unset:
            kwargs["allowed_resources"] = allowed_resources
        if duration is not unset:
            kwargs["duration"] = duration
        if excluded_resources is not unset:
            kwargs["excluded_resources"] = excluded_resources
        if fail_on_no_data is not unset:
            kwargs["fail_on_no_data"] = fail_on_no_data
        if fail_on_no_groups_found is not unset:
            kwargs["fail_on_no_groups_found"] = fail_on_no_groups_found
        if monitor_ids is not unset:
            kwargs["monitor_ids"] = monitor_ids
        if query is not unset:
            kwargs["query"] = query
        if warmup is not unset:
            kwargs["warmup"] = warmup
        super().__init__(kwargs)

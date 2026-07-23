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
    from datadog_api_client.v2.model.schedule_trigger_overlap_behavior import ScheduleTriggerOverlapBehavior


class ScheduleTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_trigger_overlap_behavior import ScheduleTriggerOverlapBehavior

        return {
            "overlap_behavior": (ScheduleTriggerOverlapBehavior,),
            "rrule_expression": (str,),
        }

    attribute_map = {
        "overlap_behavior": "overlapBehavior",
        "rrule_expression": "rruleExpression",
    }

    def __init__(
        self_,
        rrule_expression: str,
        overlap_behavior: Union[ScheduleTriggerOverlapBehavior, UnsetType] = unset,
        **kwargs,
    ):
        """
        Trigger a workflow from a Schedule. The workflow must be published.

        :param overlap_behavior: Controls whether a scheduled workflow run may start while another instance is still running.
        :type overlap_behavior: ScheduleTriggerOverlapBehavior, optional

        :param rrule_expression: Recurrence rule expression for scheduling.
        :type rrule_expression: str
        """
        if overlap_behavior is not unset:
            kwargs["overlap_behavior"] = overlap_behavior
        super().__init__(kwargs)

        self_.rrule_expression = rrule_expression

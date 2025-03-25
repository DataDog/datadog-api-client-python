# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ScheduleTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "rrule_expression": (str,),
        }

    attribute_map = {
        "rrule_expression": "rruleExpression",
    }

    def __init__(self_, rrule_expression: str, **kwargs):
        """
        Trigger a workflow from a Schedule. The workflow must be published.

        :param rrule_expression: Recurrence rule expression for scheduling.
        :type rrule_expression: str
        """
        super().__init__(kwargs)

        self_.rrule_expression = rrule_expression

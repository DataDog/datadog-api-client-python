# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScheduleOnCallRespondersDataRelationshipsRespondersDataItemsType(ModelSimple):
    """
    Identifies the resource type for a responder group linked to a schedule's on-call responders lookup.

    :param value: If omitted defaults to "schedule_oncall_responder". Must be one of ["schedule_oncall_responder"].
    :type value: str
    """

    allowed_values = {
        "schedule_oncall_responder",
    }
    SCHEDULE_ONCALL_RESPONDER: ClassVar["ScheduleOnCallRespondersDataRelationshipsRespondersDataItemsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScheduleOnCallRespondersDataRelationshipsRespondersDataItemsType.SCHEDULE_ONCALL_RESPONDER = (
    ScheduleOnCallRespondersDataRelationshipsRespondersDataItemsType("schedule_oncall_responder")
)

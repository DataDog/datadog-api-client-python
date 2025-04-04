# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay(ModelSimple):
    """
    The weekday when the restriction period starts (Monday through Sunday).

    :param value: Must be one of ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"].
    :type value: str
    """

    allowed_values = {
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    }
    MONDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    TUESDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    WEDNESDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    THURSDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    FRIDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    SATURDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    SUNDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.MONDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("monday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.TUESDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("tuesday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.WEDNESDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("wednesday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.THURSDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("thursday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.FRIDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("friday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.SATURDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("saturday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.SUNDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("sunday")
)

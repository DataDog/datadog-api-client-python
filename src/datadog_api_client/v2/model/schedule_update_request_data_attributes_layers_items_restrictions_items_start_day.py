# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay(ModelSimple):
    """
    Defines the day of the week on which the time restriction starts.

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
    MONDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    TUESDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    WEDNESDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    THURSDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    FRIDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    SATURDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]
    SUNDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.MONDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("monday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.TUESDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("tuesday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.WEDNESDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("wednesday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.THURSDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("thursday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.FRIDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("friday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.SATURDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("saturday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay.SUNDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay("sunday")
)

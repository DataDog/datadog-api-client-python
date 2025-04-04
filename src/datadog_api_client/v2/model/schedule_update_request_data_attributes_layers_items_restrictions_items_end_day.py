# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay(ModelSimple):
    """
    Defines the day of the week on which the time restriction ends.

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
    MONDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    TUESDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    WEDNESDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    THURSDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    FRIDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    SATURDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    SUNDAY: ClassVar["ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.MONDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("monday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.TUESDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("tuesday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.WEDNESDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("wednesday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.THURSDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("thursday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.FRIDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("friday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.SATURDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("saturday")
)
ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.SUNDAY = (
    ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("sunday")
)

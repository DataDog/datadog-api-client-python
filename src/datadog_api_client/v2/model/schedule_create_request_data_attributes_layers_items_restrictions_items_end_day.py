# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay(ModelSimple):
    """
    The weekday when the restriction period ends (Monday through Sunday).

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
    MONDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    TUESDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    WEDNESDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    THURSDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    FRIDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    SATURDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]
    SUNDAY: ClassVar["ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.MONDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("monday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.TUESDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("tuesday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.WEDNESDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("wednesday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.THURSDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("thursday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.FRIDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("friday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.SATURDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("saturday")
)
ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay.SUNDAY = (
    ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay("sunday")
)

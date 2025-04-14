# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LayerAttributesRestrictionsItemsStartDay(ModelSimple):
    """
    Defines the start day of the restriction within a Layer.

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
    MONDAY: ClassVar["LayerAttributesRestrictionsItemsStartDay"]
    TUESDAY: ClassVar["LayerAttributesRestrictionsItemsStartDay"]
    WEDNESDAY: ClassVar["LayerAttributesRestrictionsItemsStartDay"]
    THURSDAY: ClassVar["LayerAttributesRestrictionsItemsStartDay"]
    FRIDAY: ClassVar["LayerAttributesRestrictionsItemsStartDay"]
    SATURDAY: ClassVar["LayerAttributesRestrictionsItemsStartDay"]
    SUNDAY: ClassVar["LayerAttributesRestrictionsItemsStartDay"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LayerAttributesRestrictionsItemsStartDay.MONDAY = LayerAttributesRestrictionsItemsStartDay("monday")
LayerAttributesRestrictionsItemsStartDay.TUESDAY = LayerAttributesRestrictionsItemsStartDay("tuesday")
LayerAttributesRestrictionsItemsStartDay.WEDNESDAY = LayerAttributesRestrictionsItemsStartDay("wednesday")
LayerAttributesRestrictionsItemsStartDay.THURSDAY = LayerAttributesRestrictionsItemsStartDay("thursday")
LayerAttributesRestrictionsItemsStartDay.FRIDAY = LayerAttributesRestrictionsItemsStartDay("friday")
LayerAttributesRestrictionsItemsStartDay.SATURDAY = LayerAttributesRestrictionsItemsStartDay("saturday")
LayerAttributesRestrictionsItemsStartDay.SUNDAY = LayerAttributesRestrictionsItemsStartDay("sunday")

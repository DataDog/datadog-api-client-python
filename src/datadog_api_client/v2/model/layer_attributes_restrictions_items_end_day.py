# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LayerAttributesRestrictionsItemsEndDay(ModelSimple):
    """
    Defines the end day of the restriction within a Layer.

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
    MONDAY: ClassVar["LayerAttributesRestrictionsItemsEndDay"]
    TUESDAY: ClassVar["LayerAttributesRestrictionsItemsEndDay"]
    WEDNESDAY: ClassVar["LayerAttributesRestrictionsItemsEndDay"]
    THURSDAY: ClassVar["LayerAttributesRestrictionsItemsEndDay"]
    FRIDAY: ClassVar["LayerAttributesRestrictionsItemsEndDay"]
    SATURDAY: ClassVar["LayerAttributesRestrictionsItemsEndDay"]
    SUNDAY: ClassVar["LayerAttributesRestrictionsItemsEndDay"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LayerAttributesRestrictionsItemsEndDay.MONDAY = LayerAttributesRestrictionsItemsEndDay("monday")
LayerAttributesRestrictionsItemsEndDay.TUESDAY = LayerAttributesRestrictionsItemsEndDay("tuesday")
LayerAttributesRestrictionsItemsEndDay.WEDNESDAY = LayerAttributesRestrictionsItemsEndDay("wednesday")
LayerAttributesRestrictionsItemsEndDay.THURSDAY = LayerAttributesRestrictionsItemsEndDay("thursday")
LayerAttributesRestrictionsItemsEndDay.FRIDAY = LayerAttributesRestrictionsItemsEndDay("friday")
LayerAttributesRestrictionsItemsEndDay.SATURDAY = LayerAttributesRestrictionsItemsEndDay("saturday")
LayerAttributesRestrictionsItemsEndDay.SUNDAY = LayerAttributesRestrictionsItemsEndDay("sunday")

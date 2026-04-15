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
    from datadog_api_client.v1.model.calendar_interval_type import CalendarIntervalType


class CalendarInterval(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.calendar_interval_type import CalendarIntervalType

        return {
            "alignment": (str,),
            "quantity": (int,),
            "timezone": (str,),
            "type": (CalendarIntervalType,),
        }

    attribute_map = {
        "alignment": "alignment",
        "quantity": "quantity",
        "timezone": "timezone",
        "type": "type",
    }

    def __init__(
        self_,
        type: CalendarIntervalType,
        alignment: Union[str, UnsetType] = unset,
        quantity: Union[int, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Calendar interval definition.

        :param alignment: Alignment of the interval. Valid values depend on the interval type. For ``day`` , use hours (for example, ``1am`` , ``2pm`` , or ``14`` ). For ``week`` , use day names (for example, ``monday`` ). For ``month`` , use day-of-month ordinals (for example, ``1st`` , ``15th`` ). For ``year`` or ``quarter`` , use month names (for example, ``january`` ).
        :type alignment: str, optional

        :param quantity: Quantity of the interval.
        :type quantity: int, optional

        :param timezone: Timezone for the interval.
        :type timezone: str, optional

        :param type: Type of calendar interval.
        :type type: CalendarIntervalType
        """
        if alignment is not unset:
            kwargs["alignment"] = alignment
        if quantity is not unset:
            kwargs["quantity"] = quantity
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)

        self_.type = type

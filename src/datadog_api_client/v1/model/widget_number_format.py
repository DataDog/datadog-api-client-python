# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.number_format_unit import NumberFormatUnit
    from datadog_api_client.v1.model.number_format_unit_scale import NumberFormatUnitScale
    from datadog_api_client.v1.model.number_format_unit_canonical import NumberFormatUnitCanonical
    from datadog_api_client.v1.model.number_format_unit_custom import NumberFormatUnitCustom


class WidgetNumberFormat(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.number_format_unit import NumberFormatUnit
        from datadog_api_client.v1.model.number_format_unit_scale import NumberFormatUnitScale

        return {
            "unit": (NumberFormatUnit,),
            "unit_scale": (NumberFormatUnitScale,),
        }

    attribute_map = {
        "unit": "unit",
        "unit_scale": "unit_scale",
    }

    def __init__(
        self_,
        unit: Union[NumberFormatUnit, NumberFormatUnitCanonical, NumberFormatUnitCustom, UnsetType] = unset,
        unit_scale: Union[NumberFormatUnitScale, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Number format options for the widget.

        :param unit: Number format unit.
        :type unit: NumberFormatUnit, optional

        :param unit_scale: The definition of ``NumberFormatUnitScale`` object.
        :type unit_scale: NumberFormatUnitScale, none_type, optional
        """
        if unit is not unset:
            kwargs["unit"] = unit
        if unit_scale is not unset:
            kwargs["unit_scale"] = unit_scale
        super().__init__(kwargs)

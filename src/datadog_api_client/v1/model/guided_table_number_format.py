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
    from datadog_api_client.v1.model.guided_table_number_format_precision import GuidedTableNumberFormatPrecision
    from datadog_api_client.v1.model.number_format_unit import NumberFormatUnit
    from datadog_api_client.v1.model.number_format_unit_scale import NumberFormatUnitScale
    from datadog_api_client.v1.model.number_format_unit_canonical import NumberFormatUnitCanonical
    from datadog_api_client.v1.model.number_format_unit_custom import NumberFormatUnitCustom


class GuidedTableNumberFormat(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_number_format_precision import GuidedTableNumberFormatPrecision
        from datadog_api_client.v1.model.number_format_unit import NumberFormatUnit
        from datadog_api_client.v1.model.number_format_unit_scale import NumberFormatUnitScale

        return {
            "precision": (GuidedTableNumberFormatPrecision,),
            "unit": (NumberFormatUnit,),
            "unit_scale": (NumberFormatUnitScale,),
        }

    attribute_map = {
        "precision": "precision",
        "unit": "unit",
        "unit_scale": "unit_scale",
    }

    def __init__(
        self_,
        precision: Union[GuidedTableNumberFormatPrecision, str, int, UnsetType] = unset,
        unit: Union[NumberFormatUnit, NumberFormatUnitCanonical, NumberFormatUnitCustom, UnsetType] = unset,
        unit_scale: Union[NumberFormatUnitScale, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Number display format for a guided table column value.

        :param precision: Number of digits after the decimal point. Use ``*`` for full precision, ``integer`` to show full integer values, or omit for automatic precision.
        :type precision: GuidedTableNumberFormatPrecision, optional

        :param unit: Number format unit.
        :type unit: NumberFormatUnit, optional

        :param unit_scale: The definition of ``NumberFormatUnitScale`` object.
        :type unit_scale: NumberFormatUnitScale, none_type, optional
        """
        if precision is not unset:
            kwargs["precision"] = precision
        if unit is not unset:
            kwargs["unit"] = unit
        if unit_scale is not unset:
            kwargs["unit_scale"] = unit_scale
        super().__init__(kwargs)

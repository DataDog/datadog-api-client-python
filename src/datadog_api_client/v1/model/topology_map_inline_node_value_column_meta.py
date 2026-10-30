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
    from datadog_api_client.v1.model.number_format_unit import NumberFormatUnit
    from datadog_api_client.v1.model.number_format_unit_canonical import NumberFormatUnitCanonical
    from datadog_api_client.v1.model.number_format_unit_custom import NumberFormatUnitCustom


class TopologyMapInlineNodeValueColumnMeta(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.number_format_unit import NumberFormatUnit

        return {
            "unit": (NumberFormatUnit,),
        }

    attribute_map = {
        "unit": "unit",
    }

    def __init__(
        self_,
        unit: Union[NumberFormatUnit, NumberFormatUnitCanonical, NumberFormatUnitCustom, UnsetType] = unset,
        **kwargs,
    ):
        """
        Display options for a value column.

        :param unit: Number format unit.
        :type unit: NumberFormatUnit, optional
        """
        if unit is not unset:
            kwargs["unit"] = unit
        super().__init__(kwargs)

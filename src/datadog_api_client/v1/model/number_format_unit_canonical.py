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
    from datadog_api_client.v1.model.number_format_unit_scale_type import NumberFormatUnitScaleType


class NumberFormatUnitCanonical(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.number_format_unit_scale_type import NumberFormatUnitScaleType

        return {
            "per_unit_name": (str,),
            "type": (NumberFormatUnitScaleType,),
            "unit_name": (str,),
        }

    attribute_map = {
        "per_unit_name": "per_unit_name",
        "type": "type",
        "unit_name": "unit_name",
    }

    def __init__(
        self_,
        per_unit_name: Union[str, UnsetType] = unset,
        type: Union[NumberFormatUnitScaleType, UnsetType] = unset,
        unit_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Canonical unit.

        :param per_unit_name: The name of the unit per item.
        :type per_unit_name: str, optional

        :param type: The type of unit scale.
        :type type: NumberFormatUnitScaleType, optional

        :param unit_name: The name of the unit.
        :type unit_name: str, optional
        """
        if per_unit_name is not unset:
            kwargs["per_unit_name"] = per_unit_name
        if type is not unset:
            kwargs["type"] = type
        if unit_name is not unset:
            kwargs["unit_name"] = unit_name
        super().__init__(kwargs)

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
    from datadog_api_client.v1.model.number_format_unit_custom_type import NumberFormatUnitCustomType


class NumberFormatUnitCustom(ModelNormal):
    validations = {
        "label": {
            "max_length": 12,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.number_format_unit_custom_type import NumberFormatUnitCustomType

        return {
            "label": (str,),
            "type": (NumberFormatUnitCustomType,),
        }

    attribute_map = {
        "label": "label",
        "type": "type",
    }

    def __init__(
        self_,
        label: Union[str, UnsetType] = unset,
        type: Union[NumberFormatUnitCustomType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Custom unit.

        :param label: The label for the custom unit.
        :type label: str, optional

        :param type: The type of custom unit.
        :type type: NumberFormatUnitCustomType, optional
        """
        if label is not unset:
            kwargs["label"] = label
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ProductAnalyticsRetentionPeriod(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "unit": (str,),
            "value": (int,),
        }

    attribute_map = {
        "unit": "unit",
        "value": "value",
    }

    def __init__(self_, unit: Union[str, UnsetType] = unset, value: Union[int, UnsetType] = unset, **kwargs):
        """
        A return period definition, such as "1 week".

        :param unit: Time unit of the period, such as ``day`` , ``week`` , ``month`` , or ``year``.
        :type unit: str, optional

        :param value: Length of the period, expressed in ``unit``.
        :type value: int, optional
        """
        if unit is not unset:
            kwargs["unit"] = unit
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)

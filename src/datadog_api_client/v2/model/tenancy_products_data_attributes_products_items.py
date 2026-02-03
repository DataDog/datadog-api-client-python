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


class TenancyProductsDataAttributesProductsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
            "product_key": (str,),
        }

    attribute_map = {
        "enabled": "enabled",
        "product_key": "product_key",
    }

    def __init__(self_, enabled: Union[bool, UnsetType] = unset, product_key: Union[str, UnsetType] = unset, **kwargs):
        """


        :param enabled:
        :type enabled: bool, optional

        :param product_key:
        :type product_key: str, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if product_key is not unset:
            kwargs["product_key"] = product_key
        super().__init__(kwargs)

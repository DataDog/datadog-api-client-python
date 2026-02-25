# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_unit import ProductAnalyticsUnit


class ProductAnalyticsScalarColumnMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_unit import ProductAnalyticsUnit

        return {
            "unit": ([ProductAnalyticsUnit], none_type),
        }

    attribute_map = {
        "unit": "unit",
    }

    def __init__(self_, unit: Union[List[ProductAnalyticsUnit], none_type, UnsetType] = unset, **kwargs):
        """


        :param unit:
        :type unit: [ProductAnalyticsUnit], none_type, optional
        """
        if unit is not unset:
            kwargs["unit"] = unit
        super().__init__(kwargs)

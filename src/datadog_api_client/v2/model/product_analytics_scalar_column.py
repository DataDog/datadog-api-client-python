# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_scalar_column_meta import ProductAnalyticsScalarColumnMeta
    from datadog_api_client.v2.model.product_analytics_scalar_column_type import ProductAnalyticsScalarColumnType


class ProductAnalyticsScalarColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_scalar_column_meta import ProductAnalyticsScalarColumnMeta
        from datadog_api_client.v2.model.product_analytics_scalar_column_type import ProductAnalyticsScalarColumnType

        return {
            "meta": (ProductAnalyticsScalarColumnMeta,),
            "name": (str,),
            "type": (ProductAnalyticsScalarColumnType,),
            "values": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
        }

    attribute_map = {
        "meta": "meta",
        "name": "name",
        "type": "type",
        "values": "values",
    }

    def __init__(
        self_,
        meta: Union[ProductAnalyticsScalarColumnMeta, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        type: Union[ProductAnalyticsScalarColumnType, UnsetType] = unset,
        values: Union[List[Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        A column in a scalar response.

        :param meta:
        :type meta: ProductAnalyticsScalarColumnMeta, optional

        :param name: Column name (facet name for group-by, or "query").
        :type name: str, optional

        :param type: Column type.
        :type type: ProductAnalyticsScalarColumnType, optional

        :param values: Column values.
        :type values: [bool, date, datetime, dict, float, int, list, str, UUID, none_type], optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)

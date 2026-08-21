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
    from datadog_api_client.v2.model.product_analytics_retention_list_column_field import (
        ProductAnalyticsRetentionListColumnField,
    )


class ProductAnalyticsRetentionListColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_list_column_field import (
            ProductAnalyticsRetentionListColumnField,
        )

        return {
            "field": (ProductAnalyticsRetentionListColumnField,),
        }

    attribute_map = {
        "field": "field",
    }

    def __init__(self_, field: Union[ProductAnalyticsRetentionListColumnField, UnsetType] = unset, **kwargs):
        """
        A column to include in each returned entity row.

        :param field: The attribute selected for a column.
        :type field: ProductAnalyticsRetentionListColumnField, optional
        """
        if field is not unset:
            kwargs["field"] = field
        super().__init__(kwargs)

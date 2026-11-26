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
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder


class RetentionGroupByItemsSort(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder

        return {
            "order": (QuerySortOrder,),
        }

    attribute_map = {
        "order": "order",
    }

    def __init__(self_, order: Union[QuerySortOrder, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder, optional
        """
        if order is not unset:
            kwargs["order"] = order
        super().__init__(kwargs)

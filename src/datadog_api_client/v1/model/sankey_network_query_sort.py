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
    from datadog_api_client.v1.model.widget_sort import WidgetSort


class SankeyNetworkQuerySort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_sort import WidgetSort

        return {
            "field": (str,),
            "order": (WidgetSort,),
        }

    attribute_map = {
        "field": "field",
        "order": "order",
    }

    def __init__(self_, field: Union[str, UnsetType] = unset, order: Union[WidgetSort, UnsetType] = unset, **kwargs):
        """
        Sort configuration for network queries.

        :param field: Field to sort by.
        :type field: str, optional

        :param order: Widget sorting methods.
        :type order: WidgetSort, optional
        """
        if field is not unset:
            kwargs["field"] = field
        if order is not unset:
            kwargs["order"] = order
        super().__init__(kwargs)

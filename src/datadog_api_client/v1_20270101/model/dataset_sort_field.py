# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder


class DatasetSortField(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder

        return {
            "name": (str,),
            "order": (QuerySortOrder,),
        }

    attribute_map = {
        "name": "name",
        "order": "order",
    }

    def __init__(self_, name: str, order: QuerySortOrder, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder
        """
        super().__init__(kwargs)

        self_.name = name
        self_.order = order

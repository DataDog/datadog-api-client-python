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
    from datadog_api_client.v1_20270101.model.sort_order import SortOrder


class SortPair(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.sort_order import SortOrder

        return {
            "column": (str,),
            "order": (SortOrder,),
        }

    attribute_map = {
        "column": "column",
        "order": "order",
    }

    def __init__(self_, column: str, order: SortOrder, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: SortOrder
        """
        super().__init__(kwargs)

        self_.column = column
        self_.order = order

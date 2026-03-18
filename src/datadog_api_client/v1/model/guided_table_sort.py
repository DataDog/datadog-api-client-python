# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.widget_field_sort import WidgetFieldSort


class GuidedTableSort(ModelNormal):
    validations = {
        "limit": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_field_sort import WidgetFieldSort

        return {
            "columns": ([WidgetFieldSort],),
            "limit": (int,),
        }

    attribute_map = {
        "columns": "columns",
        "limit": "limit",
    }

    def __init__(self_, columns: List[WidgetFieldSort], limit: int, **kwargs):
        """
        Sort configuration for a guided table.

        :param columns: Columns to sort by, in order of application.
        :type columns: [WidgetFieldSort]

        :param limit: Maximum number of rows to show after sorting.
        :type limit: int
        """
        super().__init__(kwargs)

        self_.columns = columns
        self_.limit = limit

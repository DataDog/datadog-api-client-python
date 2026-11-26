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
    from datadog_api_client.v1_20270101.model.table_trend_type import TableTrendType
    from datadog_api_client.v1_20270101.model.table_trend_cell_display_mode_options_y_scale import (
        TableTrendCellDisplayModeOptionsYScale,
    )


class TableTrendCellDisplayModeOptions(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.table_trend_type import TableTrendType
        from datadog_api_client.v1_20270101.model.table_trend_cell_display_mode_options_y_scale import (
            TableTrendCellDisplayModeOptionsYScale,
        )

        return {
            "trend_type": (TableTrendType,),
            "y_scale": (TableTrendCellDisplayModeOptionsYScale,),
        }

    attribute_map = {
        "trend_type": "trend_type",
        "y_scale": "y_scale",
    }

    def __init__(self_, trend_type: TableTrendType, y_scale: TableTrendCellDisplayModeOptionsYScale, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param trend_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type trend_type: TableTrendType

        :param y_scale: Test-only generated schema for the dashboard versioning proof of concept.
        :type y_scale: TableTrendCellDisplayModeOptionsYScale
        """
        super().__init__(kwargs)

        self_.trend_type = trend_type
        self_.y_scale = y_scale

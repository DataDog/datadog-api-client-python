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
    from datadog_api_client.v1.model.widget_formula_cell_display_mode_options_trend_type import (
        WidgetFormulaCellDisplayModeOptionsTrendType,
    )
    from datadog_api_client.v1.model.widget_formula_cell_display_mode_options_y_scale import (
        WidgetFormulaCellDisplayModeOptionsYScale,
    )


class WidgetFormulaCellDisplayModeOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_formula_cell_display_mode_options_trend_type import (
            WidgetFormulaCellDisplayModeOptionsTrendType,
        )
        from datadog_api_client.v1.model.widget_formula_cell_display_mode_options_y_scale import (
            WidgetFormulaCellDisplayModeOptionsYScale,
        )

        return {
            "trend_type": (WidgetFormulaCellDisplayModeOptionsTrendType,),
            "y_scale": (WidgetFormulaCellDisplayModeOptionsYScale,),
        }

    attribute_map = {
        "trend_type": "trend_type",
        "y_scale": "y_scale",
    }

    def __init__(
        self_,
        trend_type: Union[WidgetFormulaCellDisplayModeOptionsTrendType, UnsetType] = unset,
        y_scale: Union[WidgetFormulaCellDisplayModeOptionsYScale, UnsetType] = unset,
        **kwargs,
    ):
        """
        Cell display mode options for the widget formula. (only if ``cell_display_mode`` is set to ``trend`` ).

        :param trend_type: Trend type for the cell display mode options.
        :type trend_type: WidgetFormulaCellDisplayModeOptionsTrendType, optional

        :param y_scale: Y scale for the cell display mode options.
        :type y_scale: WidgetFormulaCellDisplayModeOptionsYScale, optional
        """
        if trend_type is not unset:
            kwargs["trend_type"] = trend_type
        if y_scale is not unset:
            kwargs["y_scale"] = y_scale
        super().__init__(kwargs)

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
    from datadog_api_client.v1.model.bar_chart_widget_flat_type import BarChartWidgetFlatType


class BarChartWidgetFlat(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.bar_chart_widget_flat_type import BarChartWidgetFlatType

        return {
            "type": (BarChartWidgetFlatType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: BarChartWidgetFlatType, **kwargs):
        """
        Bar chart widget flat display.

        :param type: Bar chart widget flat display type.
        :type type: BarChartWidgetFlatType
        """
        super().__init__(kwargs)

        self_.type = type

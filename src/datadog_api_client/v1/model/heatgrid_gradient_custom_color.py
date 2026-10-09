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
    from datadog_api_client.v1.model.heatgrid_gradient_mode import HeatgridGradientMode
    from datadog_api_client.v1.model.heatgrid_custom_color_source import HeatgridCustomColorSource
    from datadog_api_client.v1.model.heatgrid_color_stop import HeatgridColorStop


class HeatgridGradientCustomColor(ModelNormal):
    validations = {
        "stops": {
            "max_items": 6,
            "min_items": 2,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_gradient_mode import HeatgridGradientMode
        from datadog_api_client.v1.model.heatgrid_custom_color_source import HeatgridCustomColorSource
        from datadog_api_client.v1.model.heatgrid_color_stop import HeatgridColorStop

        return {
            "mode": (HeatgridGradientMode,),
            "source": (HeatgridCustomColorSource,),
            "stops": ([HeatgridColorStop],),
        }

    attribute_map = {
        "mode": "mode",
        "source": "source",
        "stops": "stops",
    }

    def __init__(
        self_, mode: HeatgridGradientMode, source: HeatgridCustomColorSource, stops: List[HeatgridColorStop], **kwargs
    ):
        """
        A continuous gradient with custom color stops.

        :param mode: Use a continuous color gradient.
        :type mode: HeatgridGradientMode

        :param source: Use custom colors.
        :type source: HeatgridCustomColorSource

        :param stops: Two to six stops with positions in ascending order.
        :type stops: [HeatgridColorStop]
        """
        super().__init__(kwargs)

        self_.mode = mode
        self_.source = source
        self_.stops = stops

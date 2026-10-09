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
    from datadog_api_client.v1.model.heatgrid_color_bin import HeatgridColorBin
    from datadog_api_client.v1.model.heatgrid_discrete_mode import HeatgridDiscreteMode
    from datadog_api_client.v1.model.heatgrid_custom_color_source import HeatgridCustomColorSource


class HeatgridDiscreteCustomColor(ModelNormal):
    validations = {
        "bins": {
            "max_items": 6,
            "min_items": 2,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_color_bin import HeatgridColorBin
        from datadog_api_client.v1.model.heatgrid_discrete_mode import HeatgridDiscreteMode
        from datadog_api_client.v1.model.heatgrid_custom_color_source import HeatgridCustomColorSource

        return {
            "bins": ([HeatgridColorBin],),
            "mode": (HeatgridDiscreteMode,),
            "source": (HeatgridCustomColorSource,),
        }

    attribute_map = {
        "bins": "bins",
        "mode": "mode",
        "source": "source",
    }

    def __init__(
        self_, bins: List[HeatgridColorBin], mode: HeatgridDiscreteMode, source: HeatgridCustomColorSource, **kwargs
    ):
        """
        Discrete thresholds with custom colors.

        :param bins: Two to six bins. Omit ``lower_bound`` on the first bin. Subsequent lower bounds must be in
            ascending order.
        :type bins: [HeatgridColorBin]

        :param mode: Use discrete color thresholds.
        :type mode: HeatgridDiscreteMode

        :param source: Use custom colors.
        :type source: HeatgridCustomColorSource
        """
        super().__init__(kwargs)

        self_.bins = bins
        self_.mode = mode
        self_.source = source

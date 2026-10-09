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
    from datadog_api_client.v1.model.heatgrid_discrete_mode import HeatgridDiscreteMode
    from datadog_api_client.v1.model.heatgrid_preset_color_source import HeatgridPresetColorSource


class HeatgridDiscretePresetColor(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_discrete_mode import HeatgridDiscreteMode
        from datadog_api_client.v1.model.heatgrid_preset_color_source import HeatgridPresetColorSource

        return {
            "mode": (HeatgridDiscreteMode,),
            "preset_name": (str,),
            "source": (HeatgridPresetColorSource,),
        }

    attribute_map = {
        "mode": "mode",
        "preset_name": "preset_name",
        "source": "source",
    }

    def __init__(self_, mode: HeatgridDiscreteMode, preset_name: str, source: HeatgridPresetColorSource, **kwargs):
        """
        A preset discrete color palette.

        :param mode: Use discrete color thresholds.
        :type mode: HeatgridDiscreteMode

        :param preset_name: Name of the preset color palette.
        :type preset_name: str

        :param source: Use a preset color palette.
        :type source: HeatgridPresetColorSource
        """
        super().__init__(kwargs)

        self_.mode = mode
        self_.preset_name = preset_name
        self_.source = source

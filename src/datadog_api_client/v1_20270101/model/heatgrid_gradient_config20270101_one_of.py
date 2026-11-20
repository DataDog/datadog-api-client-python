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
    from datadog_api_client.v1_20270101.model.heatgrid_gradient_config_any_of_any_of_item_mode import (
        HeatgridGradientConfigAnyOfAnyOfItemMode,
    )
    from datadog_api_client.v1_20270101.model.heatgrid_gradient_config_any_of_any_of_item_source import (
        HeatgridGradientConfigAnyOfAnyOfItemSource,
    )
    from datadog_api_client.v1_20270101.model.heatgrid_stop import HeatgridStop


class HeatgridGradientConfig20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.heatgrid_gradient_config_any_of_any_of_item_mode import (
            HeatgridGradientConfigAnyOfAnyOfItemMode,
        )
        from datadog_api_client.v1_20270101.model.heatgrid_gradient_config_any_of_any_of_item_source import (
            HeatgridGradientConfigAnyOfAnyOfItemSource,
        )
        from datadog_api_client.v1_20270101.model.heatgrid_stop import HeatgridStop

        return {
            "mode": (HeatgridGradientConfigAnyOfAnyOfItemMode,),
            "source": (HeatgridGradientConfigAnyOfAnyOfItemSource,),
            "stops": ([HeatgridStop],),
        }

    attribute_map = {
        "mode": "mode",
        "source": "source",
        "stops": "stops",
    }

    def __init__(
        self_,
        mode: HeatgridGradientConfigAnyOfAnyOfItemMode,
        source: HeatgridGradientConfigAnyOfAnyOfItemSource,
        stops: List[HeatgridStop],
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type mode: HeatgridGradientConfigAnyOfAnyOfItemMode

        :param source: Test-only generated schema for the dashboard versioning proof of concept.
        :type source: HeatgridGradientConfigAnyOfAnyOfItemSource

        :param stops: Test-only generated schema for the dashboard versioning proof of concept.
        :type stops: [HeatgridStop]
        """
        super().__init__(kwargs)

        self_.mode = mode
        self_.source = source
        self_.stops = stops

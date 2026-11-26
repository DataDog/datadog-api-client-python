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
    from datadog_api_client.v1_20270101.model.heatgrid_bin import HeatgridBin
    from datadog_api_client.v1_20270101.model.heatgrid_discrete_config_any_of_any_of_item_mode import (
        HeatgridDiscreteConfigAnyOfAnyOfItemMode,
    )
    from datadog_api_client.v1_20270101.model.heatgrid_discrete_config_any_of_any_of_item_source import (
        HeatgridDiscreteConfigAnyOfAnyOfItemSource,
    )


class HeatgridDiscreteConfig20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.heatgrid_bin import HeatgridBin
        from datadog_api_client.v1_20270101.model.heatgrid_discrete_config_any_of_any_of_item_mode import (
            HeatgridDiscreteConfigAnyOfAnyOfItemMode,
        )
        from datadog_api_client.v1_20270101.model.heatgrid_discrete_config_any_of_any_of_item_source import (
            HeatgridDiscreteConfigAnyOfAnyOfItemSource,
        )

        return {
            "bins": ([HeatgridBin],),
            "mode": (HeatgridDiscreteConfigAnyOfAnyOfItemMode,),
            "source": (HeatgridDiscreteConfigAnyOfAnyOfItemSource,),
        }

    attribute_map = {
        "bins": "bins",
        "mode": "mode",
        "source": "source",
    }

    def __init__(
        self_,
        bins: List[HeatgridBin],
        mode: HeatgridDiscreteConfigAnyOfAnyOfItemMode,
        source: HeatgridDiscreteConfigAnyOfAnyOfItemSource,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param bins: Test-only generated schema for the dashboard versioning proof of concept.
        :type bins: [HeatgridBin]

        :param mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type mode: HeatgridDiscreteConfigAnyOfAnyOfItemMode

        :param source: Test-only generated schema for the dashboard versioning proof of concept.
        :type source: HeatgridDiscreteConfigAnyOfAnyOfItemSource
        """
        super().__init__(kwargs)

        self_.bins = bins
        self_.mode = mode
        self_.source = source

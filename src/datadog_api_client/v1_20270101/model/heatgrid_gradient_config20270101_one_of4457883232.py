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
    from datadog_api_client.v1_20270101.model.heatgrid_gradient_config_any_of_any_of_item_mode4447621888 import (
        HeatgridGradientConfigAnyOfAnyOfItemMode4447621888,
    )
    from datadog_api_client.v1_20270101.model.heatgrid_preset_name import HeatgridPresetName
    from datadog_api_client.v1_20270101.model.heatgrid_gradient_config_any_of_any_of_item_source4447622208 import (
        HeatgridGradientConfigAnyOfAnyOfItemSource4447622208,
    )


class HeatgridGradientConfig20270101OneOf4457883232(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.heatgrid_gradient_config_any_of_any_of_item_mode4447621888 import (
            HeatgridGradientConfigAnyOfAnyOfItemMode4447621888,
        )
        from datadog_api_client.v1_20270101.model.heatgrid_preset_name import HeatgridPresetName
        from datadog_api_client.v1_20270101.model.heatgrid_gradient_config_any_of_any_of_item_source4447622208 import (
            HeatgridGradientConfigAnyOfAnyOfItemSource4447622208,
        )

        return {
            "mode": (HeatgridGradientConfigAnyOfAnyOfItemMode4447621888,),
            "preset_name": (HeatgridPresetName,),
            "source": (HeatgridGradientConfigAnyOfAnyOfItemSource4447622208,),
        }

    attribute_map = {
        "mode": "mode",
        "preset_name": "preset_name",
        "source": "source",
    }

    def __init__(
        self_,
        mode: HeatgridGradientConfigAnyOfAnyOfItemMode4447621888,
        preset_name: HeatgridPresetName,
        source: HeatgridGradientConfigAnyOfAnyOfItemSource4447622208,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type mode: HeatgridGradientConfigAnyOfAnyOfItemMode4447621888

        :param preset_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type preset_name: HeatgridPresetName

        :param source: Test-only generated schema for the dashboard versioning proof of concept.
        :type source: HeatgridGradientConfigAnyOfAnyOfItemSource4447622208
        """
        super().__init__(kwargs)

        self_.mode = mode
        self_.preset_name = preset_name
        self_.source = source

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class HeatgridColorConfig(ModelComposed):
    def __init__(self, **kwargs):
        """
        Color configuration for continuous gradients or discrete thresholds.

        :param mode: Use a continuous color gradient.
        :type mode: HeatgridGradientMode

        :param source: Use custom colors.
        :type source: HeatgridCustomColorSource

        :param stops: Two to six stops with positions in ascending order.
        :type stops: [HeatgridColorStop]

        :param preset_name: Name of the preset color palette.
        :type preset_name: str

        :param bins: Two to six bins. Omit `lower_bound` on the first bin. Subsequent lower bounds must be in
            ascending order.
        :type bins: [HeatgridColorBin]
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.heatgrid_gradient_custom_color import HeatgridGradientCustomColor
        from datadog_api_client.v1.model.heatgrid_gradient_preset_color import HeatgridGradientPresetColor
        from datadog_api_client.v1.model.heatgrid_discrete_custom_color import HeatgridDiscreteCustomColor
        from datadog_api_client.v1.model.heatgrid_discrete_preset_color import HeatgridDiscretePresetColor

        return {
            "oneOf": [
                HeatgridGradientCustomColor,
                HeatgridGradientPresetColor,
                HeatgridDiscreteCustomColor,
                HeatgridDiscretePresetColor,
            ],
        }

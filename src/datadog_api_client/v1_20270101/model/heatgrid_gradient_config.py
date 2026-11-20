# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class HeatgridGradientConfig(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type mode: HeatgridGradientConfigAnyOfAnyOfItemMode

        :param source: Test-only generated schema for the dashboard versioning proof of concept.
        :type source: HeatgridGradientConfigAnyOfAnyOfItemSource

        :param stops: Test-only generated schema for the dashboard versioning proof of concept.
        :type stops: [HeatgridStop]

        :param preset_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type preset_name: HeatgridPresetName
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
        from datadog_api_client.v1_20270101.model.heatgrid_gradient_config20270101_one_of import (
            HeatgridGradientConfig20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.heatgrid_gradient_config20270101_one_of4457883232 import (
            HeatgridGradientConfig20270101OneOf4457883232,
        )

        return {
            "oneOf": [
                HeatgridGradientConfig20270101OneOf,
                HeatgridGradientConfig20270101OneOf4457883232,
            ],
        }

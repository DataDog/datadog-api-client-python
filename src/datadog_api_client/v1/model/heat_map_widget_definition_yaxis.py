# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class HeatMapWidgetDefinitionYaxis(ModelComposed):
    def __init__(self, **kwargs):
        """


        :param include_zero: Set to `true` to include zero.
        :type include_zero: bool, optional

        :param label: The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
        :type label: str, optional

        :param max: Specifies maximum numeric value to show on the axis. Defaults to `auto`.
        :type max: str, optional

        :param min: Specifies minimum numeric value to show on the axis. Defaults to `auto`.
        :type min: str, optional

        :param scale: Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
        :type scale: str, optional

        :param num_buckets: Number of value buckets to target, aka the resolution of the value bins.
        :type num_buckets: int, optional
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
        from datadog_api_client.v1.model.widget_axis import WidgetAxis
        from datadog_api_client.v1.model.heat_map_widget_y_axis import HeatMapWidgetYAxis

        return {
            "oneOf": [
                WidgetAxis,
                HeatMapWidgetYAxis,
            ],
        }

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TimeseriesBackground(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.timeseries_background_type import TimeseriesBackgroundType
        from datadog_api_client.v1.model.widget_axis import WidgetAxis

        return {
            "type": (TimeseriesBackgroundType,),
            "yaxis": (WidgetAxis,),
        }

    attribute_map = {
        "type": "type",
        "yaxis": "yaxis",
    }

    def __init__(self_, type, *args, **kwargs):
        """
        Set a timeseries on the widget background.

        :param type: Timeseries is made using an area or bars.
        :type type: TimeseriesBackgroundType

        :param yaxis: Axis controls for the widget.
        :type yaxis: WidgetAxis, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.type = type

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.widget_comparator import WidgetComparator
    from datadog_api_client.v1.model.widget_palette import WidgetPalette

    globals()["WidgetComparator"] = WidgetComparator
    globals()["WidgetPalette"] = WidgetPalette


class WidgetConditionalFormat(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "comparator": (WidgetComparator,),
            "custom_bg_color": (str,),
            "custom_fg_color": (str,),
            "hide_value": (bool,),
            "image_url": (str,),
            "metric": (str,),
            "palette": (WidgetPalette,),
            "timeframe": (str,),
            "value": (float,),
        }

    attribute_map = {
        "comparator": "comparator",
        "custom_bg_color": "custom_bg_color",
        "custom_fg_color": "custom_fg_color",
        "hide_value": "hide_value",
        "image_url": "image_url",
        "metric": "metric",
        "palette": "palette",
        "timeframe": "timeframe",
        "value": "value",
    }

    def __init__(self, comparator, palette, value, *args, **kwargs):
        """
        Define a conditional format for the widget.

        :param comparator: Comparator to apply.
        :type comparator: WidgetComparator

        :param custom_bg_color: Color palette to apply to the background, same values available as palette.
        :type custom_bg_color: str, optional

        :param custom_fg_color: Color palette to apply to the foreground, same values available as palette.
        :type custom_fg_color: str, optional

        :param hide_value: True hides values.
        :type hide_value: bool, optional

        :param image_url: Displays an image as the background.
        :type image_url: str, optional

        :param metric: Metric from the request to correlate this conditional format with.
        :type metric: str, optional

        :param palette: Color palette to apply.
        :type palette: WidgetPalette

        :param timeframe: Defines the displayed timeframe.
        :type timeframe: str, optional

        :param value: Value for the comparator.
        :type value: float
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.comparator = comparator
        self.palette = palette
        self.value = value

    @classmethod
    def _from_openapi_data(cls, comparator, palette, value, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetConditionalFormat, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.comparator = comparator
        self.palette = palette
        self.value = value
        return self

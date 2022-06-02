# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SunburstWidgetLegendInlineAutomatic(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.sunburst_widget_legend_inline_automatic_type import (
            SunburstWidgetLegendInlineAutomaticType,
        )

        return {
            "hide_percent": (bool,),
            "hide_value": (bool,),
            "type": (SunburstWidgetLegendInlineAutomaticType,),
        }

    attribute_map = {
        "hide_percent": "hide_percent",
        "hide_value": "hide_value",
        "type": "type",
    }

    def __init__(self, type, *args, **kwargs):
        """
        Configuration of inline or automatic legends.

        :param hide_percent: Whether to hide the percentages of the groups.
        :type hide_percent: bool, optional

        :param hide_value: Whether to hide the values of the groups.
        :type hide_value: bool, optional

        :param type: Whether to show the legend inline or let it be automatically generated.
        :type type: SunburstWidgetLegendInlineAutomaticType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SunburstWidgetLegendInlineAutomatic, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self

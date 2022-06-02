# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WidgetRequestStyle(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_line_type import WidgetLineType
        from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth

        return {
            "line_type": (WidgetLineType,),
            "line_width": (WidgetLineWidth,),
            "palette": (str,),
        }

    attribute_map = {
        "line_type": "line_type",
        "line_width": "line_width",
        "palette": "palette",
    }

    def __init__(self, *args, **kwargs):
        """
        Define request widget style.

        :param line_type: Type of lines displayed.
        :type line_type: WidgetLineType, optional

        :param line_width: Width of line displayed.
        :type line_width: WidgetLineWidth, optional

        :param palette: Color palette to apply to the widget.
        :type palette: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetRequestStyle, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

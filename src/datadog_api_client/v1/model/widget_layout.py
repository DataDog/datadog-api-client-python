# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WidgetLayout(ModelNormal):
    validations = {
        "height": {
            "inclusive_minimum": 0,
        },
        "width": {
            "inclusive_minimum": 0,
        },
        "x": {
            "inclusive_minimum": 0,
        },
        "y": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "height": (int,),
            "is_column_break": (bool,),
            "width": (int,),
            "x": (int,),
            "y": (int,),
        }

    attribute_map = {
        "height": "height",
        "is_column_break": "is_column_break",
        "width": "width",
        "x": "x",
        "y": "y",
    }

    def __init__(self, height, width, x, y, *args, **kwargs):
        """
        The layout for a widget on a ``free`` or **new dashboard layout** dashboard.

        :param height: The height of the widget. Should be a non-negative integer.
        :type height: int

        :param is_column_break: Whether the widget should be the first one on the second column in high density or not.
            **Note** : Only for the **new dashboard layout** and only one widget in the dashboard should have this property set to ``true``.
        :type is_column_break: bool, optional

        :param width: The width of the widget. Should be a non-negative integer.
        :type width: int

        :param x: The position of the widget on the x (horizontal) axis. Should be a non-negative integer.
        :type x: int

        :param y: The position of the widget on the y (vertical) axis. Should be a non-negative integer.
        :type y: int
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @classmethod
    def _from_openapi_data(cls, height, width, x, y, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetLayout, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.height = height
        self.width = width
        self.x = x
        self.y = y
        return self

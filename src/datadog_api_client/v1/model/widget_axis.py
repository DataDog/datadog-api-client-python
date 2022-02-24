# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class WidgetAxis(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "include_zero": (bool,),
            "label": (str,),
            "max": (str,),
            "min": (str,),
            "scale": (str,),
        }

    attribute_map = {
        "include_zero": "include_zero",
        "label": "label",
        "max": "max",
        "min": "min",
        "scale": "scale",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Axis controls for the widget.

        :param include_zero: True includes zero.
        :type include_zero: bool, optional

        :param label: The label of the axis to display on the graph.
        :type label: str, optional

        :param max: Specifies the maximum value to show on the y-axis. It takes a number, or auto for default behavior.
        :type max: str, optional

        :param min: Specifies minimum value to show on the y-axis. It takes a number, or auto for default behavior.
        :type min: str, optional

        :param scale: Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, `pow##` (for example `pow2`, `pow0.5` etc.).
        :type scale: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetAxis, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HostMapWidgetDefinitionStyle(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "fill_max": (str,),
            "fill_min": (str,),
            "palette": (str,),
            "palette_flip": (bool,),
        }

    attribute_map = {
        "fill_max": "fill_max",
        "fill_min": "fill_min",
        "palette": "palette",
        "palette_flip": "palette_flip",
    }

    def __init__(self, *args, **kwargs):
        """
        The style to apply to the widget.

        :param fill_max: Max value to use to color the map.
        :type fill_max: str, optional

        :param fill_min: Min value to use to color the map.
        :type fill_min: str, optional

        :param palette: Color palette to apply to the widget.
        :type palette: str, optional

        :param palette_flip: Whether to flip the palette tones.
        :type palette_flip: bool, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HostMapWidgetDefinitionStyle, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

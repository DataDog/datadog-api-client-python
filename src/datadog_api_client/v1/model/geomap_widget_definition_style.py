# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GeomapWidgetDefinitionStyle(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "palette": (str,),
            "palette_flip": (bool,),
        }

    attribute_map = {
        "palette": "palette",
        "palette_flip": "palette_flip",
    }

    def __init__(self, palette, palette_flip, *args, **kwargs):
        """
        The style to apply to the widget.

        :param palette: The color palette to apply to the widget.
        :type palette: str

        :param palette_flip: Whether to flip the palette tones.
        :type palette_flip: bool
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.palette = palette
        self.palette_flip = palette_flip

    @classmethod
    def _from_openapi_data(cls, palette, palette_flip, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(GeomapWidgetDefinitionStyle, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.palette = palette
        self.palette_flip = palette_flip
        return self

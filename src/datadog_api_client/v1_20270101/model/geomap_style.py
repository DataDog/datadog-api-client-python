# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.geomap_style_palette import GeomapStylePalette


class GeomapStyle(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.geomap_style_palette import GeomapStylePalette

        return {
            "palette": (GeomapStylePalette,),
            "palette_flip": (bool,),
        }

    attribute_map = {
        "palette": "palette",
        "palette_flip": "palette_flip",
    }

    def __init__(self_, palette: GeomapStylePalette, palette_flip: bool, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: GeomapStylePalette

        :param palette_flip: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette_flip: bool
        """
        super().__init__(kwargs)

        self_.palette = palette
        self_.palette_flip = palette_flip

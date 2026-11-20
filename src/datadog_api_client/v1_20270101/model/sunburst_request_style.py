# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.sunburst_request_style_palette import SunburstRequestStylePalette


class SunburstRequestStyle(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.sunburst_request_style_palette import SunburstRequestStylePalette

        return {
            "palette": (SunburstRequestStylePalette,),
        }

    attribute_map = {
        "palette": "palette",
    }

    def __init__(self_, palette: Union[SunburstRequestStylePalette, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: SunburstRequestStylePalette, optional
        """
        if palette is not unset:
            kwargs["palette"] = palette
        super().__init__(kwargs)

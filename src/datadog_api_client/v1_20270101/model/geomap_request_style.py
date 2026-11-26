# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GeomapRequestStyle(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "color_by": (str,),
            "palette": (str,),
        }

    attribute_map = {
        "color_by": "color_by",
        "palette": "palette",
    }

    def __init__(self_, color_by: Union[str, UnsetType] = unset, palette: Union[str, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param color_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type color_by: str, optional

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: str, optional
        """
        if color_by is not unset:
            kwargs["color_by"] = color_by
        if palette is not unset:
            kwargs["palette"] = palette
        super().__init__(kwargs)

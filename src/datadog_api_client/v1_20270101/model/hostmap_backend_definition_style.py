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


class HostmapBackendDefinitionStyle(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

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

    def __init__(
        self_,
        fill_max: Union[str, UnsetType] = unset,
        fill_min: Union[str, UnsetType] = unset,
        palette: Union[str, UnsetType] = unset,
        palette_flip: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param fill_max: Test-only generated schema for the dashboard versioning proof of concept.
        :type fill_max: str, optional

        :param fill_min: Test-only generated schema for the dashboard versioning proof of concept.
        :type fill_min: str, optional

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: str, optional

        :param palette_flip: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette_flip: bool, optional
        """
        if fill_max is not unset:
            kwargs["fill_max"] = fill_max
        if fill_min is not unset:
            kwargs["fill_min"] = fill_min
        if palette is not unset:
            kwargs["palette"] = palette
        if palette_flip is not unset:
            kwargs["palette_flip"] = palette_flip
        super().__init__(kwargs)

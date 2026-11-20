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


class WidgetFormulaStyle(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "palette": (str,),
            "palette_index": (float,),
        }

    attribute_map = {
        "palette": "palette",
        "palette_index": "palette_index",
    }

    def __init__(self_, palette: str, palette_index: Union[float, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: str

        :param palette_index: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette_index: float, optional
        """
        if palette_index is not unset:
            kwargs["palette_index"] = palette_index
        super().__init__(kwargs)

        self_.palette = palette

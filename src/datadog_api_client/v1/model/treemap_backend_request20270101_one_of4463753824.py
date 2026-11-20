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


class TreemapBackendRequest20270101OneOf4463753824(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "q": (str,),
            "style": (TreemapRequestStyle,),
        }

    attribute_map = {
        "q": "q",
        "style": "style",
    }

    def __init__(self_, q: str, style: Union[TreemapRequestStyle, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: TreemapRequestStyle, optional
        """
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.q = q

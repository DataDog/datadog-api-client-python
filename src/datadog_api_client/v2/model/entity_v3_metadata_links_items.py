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


class EntityV3MetadataLinksItems(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "provider": (str,),
            "type": (str,),
            "url": (str,),
        }

    attribute_map = {
        "name": "name",
        "provider": "provider",
        "type": "type",
        "url": "url",
    }

    def __init__(self_, name: str, url: str, provider: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of Entity V3 Metadata Links Items object.

        :param name: Link name
        :type name: str

        :param provider: Link provider.
        :type provider: str, optional

        :param type: Link type.
        :type type: str

        :param url: Link url
        :type url: str
        """
        if provider is not unset:
            kwargs["provider"] = provider
        super().__init__(kwargs)
        type = kwargs.get("type", "other")

        self_.name = name
        self_.type = type
        self_.url = url

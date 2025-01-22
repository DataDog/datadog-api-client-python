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


class SBOMMetadataComponent(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, type: Union[str, UnsetType] = unset, **kwargs):
        """
        The component that the BOM describes.

        :param name: The name of the component. This will often be a shortened, single name of the component.
        :type name: str, optional

        :param type: Specifies the type of the component.
        :type type: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

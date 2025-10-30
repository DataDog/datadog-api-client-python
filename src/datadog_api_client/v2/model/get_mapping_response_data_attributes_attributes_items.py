# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GetMappingResponseDataAttributesAttributesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attribute": (str,),
            "description": (str,),
            "display_name": (str,),
            "groups": ([str],),
            "is_custom": (bool,),
            "type": (str,),
        }

    attribute_map = {
        "attribute": "attribute",
        "description": "description",
        "display_name": "display_name",
        "groups": "groups",
        "is_custom": "is_custom",
        "type": "type",
    }

    def __init__(
        self_,
        attribute: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        groups: Union[List[str], UnsetType] = unset,
        is_custom: Union[bool, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attribute:
        :type attribute: str, optional

        :param description:
        :type description: str, optional

        :param display_name:
        :type display_name: str, optional

        :param groups:
        :type groups: [str], optional

        :param is_custom:
        :type is_custom: bool, optional

        :param type:
        :type type: str, optional
        """
        if attribute is not unset:
            kwargs["attribute"] = attribute
        if description is not unset:
            kwargs["description"] = description
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if groups is not unset:
            kwargs["groups"] = groups
        if is_custom is not unset:
            kwargs["is_custom"] = is_custom
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

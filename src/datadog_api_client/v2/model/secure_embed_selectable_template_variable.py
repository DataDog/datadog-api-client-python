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


class SecureEmbedSelectableTemplateVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "default_values": ([str],),
            "name": (str,),
            "prefix": (str,),
            "visible_tags": ([str],),
        }

    attribute_map = {
        "default_values": "default_values",
        "name": "name",
        "prefix": "prefix",
        "visible_tags": "visible_tags",
    }

    def __init__(
        self_,
        default_values: Union[List[str], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        prefix: Union[str, UnsetType] = unset,
        visible_tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A template variable that viewers can modify on the secure embed shared dashboard.

        :param default_values: Default selected values for the variable.
        :type default_values: [str], optional

        :param name: Name of the template variable. Usually matches the prefix unless you want a different display name.
        :type name: str, optional

        :param prefix: Tag prefix for the variable (e.g., ``environment`` , ``service`` ).
        :type prefix: str, optional

        :param visible_tags: Restrict which tag values are visible to the viewer.
        :type visible_tags: [str], optional
        """
        if default_values is not unset:
            kwargs["default_values"] = default_values
        if name is not unset:
            kwargs["name"] = name
        if prefix is not unset:
            kwargs["prefix"] = prefix
        if visible_tags is not unset:
            kwargs["visible_tags"] = visible_tags
        super().__init__(kwargs)

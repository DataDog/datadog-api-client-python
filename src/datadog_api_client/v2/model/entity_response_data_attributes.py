# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class EntityResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "api_version": (str,),
            "description": (str,),
            "display_name": (str,),
            "kind": (str,),
            "name": (str,),
            "namespace": (str,),
            "owner": (str,),
            "properties": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "tags": ([str],),
        }

    attribute_map = {
        "api_version": "apiVersion",
        "description": "description",
        "display_name": "displayName",
        "kind": "kind",
        "name": "name",
        "namespace": "namespace",
        "owner": "owner",
        "properties": "properties",
        "tags": "tags",
    }

    def __init__(
        self_,
        api_version: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        kind: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        namespace: Union[str, UnsetType] = unset,
        owner: Union[str, UnsetType] = unset,
        properties: Union[Dict[str, Any], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param api_version:
        :type api_version: str, optional

        :param description:
        :type description: str, optional

        :param display_name:
        :type display_name: str, optional

        :param kind:
        :type kind: str, optional

        :param name:
        :type name: str, optional

        :param namespace:
        :type namespace: str, optional

        :param owner:
        :type owner: str, optional

        :param properties:
        :type properties: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param tags:
        :type tags: [str], optional
        """
        if api_version is not unset:
            kwargs["api_version"] = api_version
        if description is not unset:
            kwargs["description"] = description
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if kind is not unset:
            kwargs["kind"] = kind
        if name is not unset:
            kwargs["name"] = name
        if namespace is not unset:
            kwargs["namespace"] = namespace
        if owner is not unset:
            kwargs["owner"] = owner
        if properties is not unset:
            kwargs["properties"] = properties
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

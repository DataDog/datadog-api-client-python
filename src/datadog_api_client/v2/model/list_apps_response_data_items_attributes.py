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


class ListAppsResponseDataItemsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "favorite": (bool,),
            "name": (str,),
            "self_service": (bool,),
            "tags": ([str],),
        }

    attribute_map = {
        "description": "description",
        "favorite": "favorite",
        "name": "name",
        "self_service": "selfService",
        "tags": "tags",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        favorite: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        self_service: Union[bool, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ListAppsResponseDataItemsAttributes`` object.

        :param description: The ``attributes`` ``description``.
        :type description: str, optional

        :param favorite: The ``attributes`` ``favorite``.
        :type favorite: bool, optional

        :param name: The ``attributes`` ``name``.
        :type name: str, optional

        :param self_service: The ``attributes`` ``selfService``.
        :type self_service: bool, optional

        :param tags: The ``attributes`` ``tags``.
        :type tags: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if favorite is not unset:
            kwargs["favorite"] = favorite
        if name is not unset:
            kwargs["name"] = name
        if self_service is not unset:
            kwargs["self_service"] = self_service
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

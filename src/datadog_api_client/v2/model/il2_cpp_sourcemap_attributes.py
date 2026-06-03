# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class IL2CPPSourcemapAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "build_id": (str,),
            "created_at": (datetime,),
            "mapkind": (str,),
            "size": (int,),
        }

    attribute_map = {
        "build_id": "build_id",
        "created_at": "created_at",
        "mapkind": "mapkind",
        "size": "size",
    }

    def __init__(
        self_, created_at: datetime, mapkind: str, size: int, build_id: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Attributes of an IL2CPP mapping file.

        :param build_id: The build identifier (UUID format).
        :type build_id: str, optional

        :param created_at: The timestamp when the mapping file was created.
        :type created_at: datetime

        :param mapkind: The type of source map.
        :type mapkind: str

        :param size: The size of the mapping file in bytes.
        :type size: int
        """
        if build_id is not unset:
            kwargs["build_id"] = build_id
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.mapkind = mapkind
        self_.size = size

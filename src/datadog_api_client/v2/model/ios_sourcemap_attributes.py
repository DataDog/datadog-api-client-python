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


class IOSSourcemapAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "mapkind": (str,),
            "size": (int,),
            "uuids": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "mapkind": "mapkind",
        "size": "size",
        "uuids": "uuids",
    }

    def __init__(self_, created_at: datetime, mapkind: str, size: int, uuids: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes of an iOS dSYM source map.

        :param created_at: The timestamp when the source map was created.
        :type created_at: datetime

        :param mapkind: The type of source map.
        :type mapkind: str

        :param size: The size of the dSYM file in bytes.
        :type size: int

        :param uuids: The UUID(s) associated with the dSYM file.
        :type uuids: str, optional
        """
        if uuids is not unset:
            kwargs["uuids"] = uuids
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.mapkind = mapkind
        self_.size = size

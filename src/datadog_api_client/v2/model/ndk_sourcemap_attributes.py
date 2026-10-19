# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ndk_sourcemap_map_kind import NDKSourcemapMapKind


class NDKSourcemapAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ndk_sourcemap_map_kind import NDKSourcemapMapKind

        return {
            "arch": (str,),
            "build_id": (str,),
            "created_at": (datetime,),
            "file_name": (str,),
            "mapkind": (NDKSourcemapMapKind,),
            "size": (int,),
        }

    attribute_map = {
        "arch": "arch",
        "build_id": "build_id",
        "created_at": "created_at",
        "file_name": "file_name",
        "mapkind": "mapkind",
        "size": "size",
    }

    def __init__(
        self_,
        created_at: datetime,
        mapkind: NDKSourcemapMapKind,
        size: int,
        arch: Union[str, UnsetType] = unset,
        build_id: Union[str, UnsetType] = unset,
        file_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an Android NDK symbol file.

        :param arch: The target CPU architecture.
        :type arch: str, optional

        :param build_id: The build identifier (UUID format).
        :type build_id: str, optional

        :param created_at: The timestamp when the symbol file was created.
        :type created_at: datetime

        :param file_name: The NDK library file name.
        :type file_name: str, optional

        :param mapkind: The type of source map. Always ``ndk`` for Android NDK source maps.
        :type mapkind: NDKSourcemapMapKind

        :param size: The size of the symbol file in bytes.
        :type size: int
        """
        if arch is not unset:
            kwargs["arch"] = arch
        if build_id is not unset:
            kwargs["build_id"] = build_id
        if file_name is not unset:
            kwargs["file_name"] = file_name
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.mapkind = mapkind
        self_.size = size

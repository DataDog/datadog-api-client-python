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


class ELFSourcemapAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arch": (str,),
            "created_at": (datetime,),
            "file_hash": (str,),
            "file_name": (str,),
            "gnu_build_id": (str,),
            "go_build_id": (str,),
            "mapkind": (str,),
            "origin": (str,),
            "origin_version": (str,),
            "size": (int,),
            "symbol_source": (str,),
        }

    attribute_map = {
        "arch": "arch",
        "created_at": "created_at",
        "file_hash": "file_hash",
        "file_name": "file_name",
        "gnu_build_id": "gnu_build_id",
        "go_build_id": "go_build_id",
        "mapkind": "mapkind",
        "origin": "origin",
        "origin_version": "origin_version",
        "size": "size",
        "symbol_source": "symbol_source",
    }

    def __init__(
        self_,
        created_at: datetime,
        mapkind: str,
        size: int,
        arch: Union[str, UnsetType] = unset,
        file_hash: Union[str, UnsetType] = unset,
        file_name: Union[str, UnsetType] = unset,
        gnu_build_id: Union[str, UnsetType] = unset,
        go_build_id: Union[str, UnsetType] = unset,
        origin: Union[str, UnsetType] = unset,
        origin_version: Union[str, UnsetType] = unset,
        symbol_source: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an ELF symbol file.

        :param arch: The target CPU architecture.
        :type arch: str, optional

        :param created_at: The timestamp when the symbol file was created.
        :type created_at: datetime

        :param file_hash: The SHA256 hash of the ELF file.
        :type file_hash: str, optional

        :param file_name: The ELF file name.
        :type file_name: str, optional

        :param gnu_build_id: The GNU build ID (UUID format).
        :type gnu_build_id: str, optional

        :param go_build_id: The Go build ID (UUID format).
        :type go_build_id: str, optional

        :param mapkind: The type of source map.
        :type mapkind: str

        :param origin: The origin of the ELF file.
        :type origin: str, optional

        :param origin_version: The version of the origin package.
        :type origin_version: str, optional

        :param size: The size of the ELF file in bytes.
        :type size: int

        :param symbol_source: The source of the debug symbols.
        :type symbol_source: str, optional
        """
        if arch is not unset:
            kwargs["arch"] = arch
        if file_hash is not unset:
            kwargs["file_hash"] = file_hash
        if file_name is not unset:
            kwargs["file_name"] = file_name
        if gnu_build_id is not unset:
            kwargs["gnu_build_id"] = gnu_build_id
        if go_build_id is not unset:
            kwargs["go_build_id"] = go_build_id
        if origin is not unset:
            kwargs["origin"] = origin
        if origin_version is not unset:
            kwargs["origin_version"] = origin_version
        if symbol_source is not unset:
            kwargs["symbol_source"] = symbol_source
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.mapkind = mapkind
        self_.size = size

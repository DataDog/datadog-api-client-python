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
    from datadog_api_client.v2.model.portable_pdb_sourcemap_map_kind import PortablePdbSourcemapMapKind


class PortablePdbSourcemapAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.portable_pdb_sourcemap_map_kind import PortablePdbSourcemapMapKind

        return {
            "build_id": (str,),
            "created_at": (datetime,),
            "file_name": (str,),
            "mapkind": (PortablePdbSourcemapMapKind,),
            "size": (int,),
        }

    attribute_map = {
        "build_id": "build_id",
        "created_at": "created_at",
        "file_name": "file_name",
        "mapkind": "mapkind",
        "size": "size",
    }

    def __init__(
        self_,
        mapkind: PortablePdbSourcemapMapKind,
        build_id: Union[str, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        file_name: Union[str, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Portable PDB file.

        :param build_id: The build identifier.
        :type build_id: str, optional

        :param created_at: The timestamp when the symbol file was created.
        :type created_at: datetime, optional

        :param file_name: The file name of the symbol file.
        :type file_name: str, optional

        :param mapkind: The type of source map. Always ``portable_pdb`` for Portable PDB files.
        :type mapkind: PortablePdbSourcemapMapKind

        :param size: The size of the symbol file in bytes.
        :type size: int, optional
        """
        if build_id is not unset:
            kwargs["build_id"] = build_id
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if file_name is not unset:
            kwargs["file_name"] = file_name
        if size is not unset:
            kwargs["size"] = size
        super().__init__(kwargs)

        self_.mapkind = mapkind

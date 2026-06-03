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


class JVMSourcemapAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "build_id": (str,),
            "created_at": (datetime,),
            "mapkind": (str,),
            "service": (str,),
            "size": (int,),
            "variant": (str,),
            "version": (str,),
            "version_code": (str,),
        }

    attribute_map = {
        "build_id": "build_id",
        "created_at": "created_at",
        "mapkind": "mapkind",
        "service": "service",
        "size": "size",
        "variant": "variant",
        "version": "version",
        "version_code": "version_code",
    }

    def __init__(
        self_,
        created_at: datetime,
        mapkind: str,
        size: int,
        build_id: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        variant: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        version_code: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a JVM mapping file.

        :param build_id: The build identifier (UUID format).
        :type build_id: str, optional

        :param created_at: The timestamp when the mapping file was created.
        :type created_at: datetime

        :param mapkind: The type of source map.
        :type mapkind: str

        :param service: The service name associated with the mapping file.
        :type service: str, optional

        :param size: The size of the mapping file in bytes.
        :type size: int

        :param variant: The build variant (e.g., ``release`` , ``debug`` ).
        :type variant: str, optional

        :param version: The version of the service associated with the mapping file.
        :type version: str, optional

        :param version_code: The version code.
        :type version_code: str, optional
        """
        if build_id is not unset:
            kwargs["build_id"] = build_id
        if service is not unset:
            kwargs["service"] = service
        if variant is not unset:
            kwargs["variant"] = variant
        if version is not unset:
            kwargs["version"] = version
        if version_code is not unset:
            kwargs["version_code"] = version_code
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.mapkind = mapkind
        self_.size = size

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


class FlutterSourcemapAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arch": (str,),
            "created_at": (datetime,),
            "mapkind": (str,),
            "service": (str,),
            "size": (int,),
            "variant": (str,),
            "version": (str,),
        }

    attribute_map = {
        "arch": "arch",
        "created_at": "created_at",
        "mapkind": "mapkind",
        "service": "service",
        "size": "size",
        "variant": "variant",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: datetime,
        mapkind: str,
        size: int,
        arch: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        variant: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Flutter symbol file.

        :param arch: The target CPU architecture.
        :type arch: str, optional

        :param created_at: The timestamp when the symbol file was created.
        :type created_at: datetime

        :param mapkind: The type of source map.
        :type mapkind: str

        :param service: The service name associated with the symbol file.
        :type service: str, optional

        :param size: The size of the symbol file in bytes.
        :type size: int

        :param variant: The build variant.
        :type variant: str, optional

        :param version: The version of the service associated with the symbol file.
        :type version: str, optional
        """
        if arch is not unset:
            kwargs["arch"] = arch
        if service is not unset:
            kwargs["service"] = service
        if variant is not unset:
            kwargs["variant"] = variant
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.mapkind = mapkind
        self_.size = size
